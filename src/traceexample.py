import sys
from types import FrameType
from mylib import say_hello

# Define the trace functions
def tracefunc(frame: FrameType, event, arg):

    calling_frame_names = []
    max_depth = 5
    current_depth = 0
    p_frame = frame.f_back
    while p_frame and p_frame.f_code.co_name != '<module>' and max_depth > current_depth:
        calling_frame_names.append(p_frame.f_code.co_name)
        p_frame = p_frame.f_back
        current_depth += 1
    calling_frame_names.reverse()

    print(f"Call stack: {' > '.join(calling_frame_names) if len(calling_frame_names) > 0 else 'None'} || Line No: {frame.f_lineno} || Locals: {frame.f_locals} || Event: {event}")

# Set the trace function
sys.settrace(tracefunc)

say_hello("John", "Doe")

sys.settrace(None)  # Disable the trace function