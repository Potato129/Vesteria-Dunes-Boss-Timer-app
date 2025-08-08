
#stripped down version of the spawn logic
#removed the main loop, I/O logic, and removed the keyboard module to avoid compatability issues
#this is a simple function to find the next boss spawn time based on the current time and the predefined spawn schedule
import datetime

spawn_schedule = {
    "Toni": [15, 35, 55],
    "Auktufiti": [0, 20, 40],
    "Azariah": [5, 25, 45],
    "Sarakis": [10, 30, 50],
}

# Function to find the next boss spawn time
# Returns a tuple of (next_spawn_time, boss_name)
def find_candidate(now=None, schedule=spawn_schedule):
    if now is None:
        now = datetime.datetime.now()
    # adds future spawn times to a candidates list
    candidates = []
    for boss, minutes in schedule.items(): 
        for m in minutes:
            hour = now.hour if now.minute < m else (now.hour + 1) % 24 
            spawn_time = now.replace(hour=hour, minute=m, second=0, microsecond=0)
         # Accounts for the case where the spawn time is in the past (i.e., when the recalculated time is earlier than 'now')
         #could be due to lag or time shaved by the replacement 
            if spawn_time < now:
                print(f"⚠ Missed {boss}'s spawn at {spawn_time.strftime('%I:%M:%S %p')}!")
                continue
            candidates.append((spawn_time, boss)) 

    return min(candidates, key=lambda x: x[0])