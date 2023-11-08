from typing import List, Dict


class WorkSchedule:
    start_time = '09:00'
    end_time = '21:00'

    def __init__(self, scheduled_time: List[Dict[str, str]]):
        self.busy_time = scheduled_time
        self.free_windows = []

    def _time_to_minutes(self, time: str) -> int:
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes

    def _minutes_to_time(self, minutes: int) -> str:
        hours = minutes // 60
        minutes = minutes % 60
        return f'{hours:02d}:{minutes:02d}'

    def get_daily_schedule(self) -> List[Dict[str, str]]:
        current_time = self._time_to_minutes(self.start_time)

        for interval in busy:
            start = self._time_to_minutes(interval['start'])
            stop = self._time_to_minutes(interval['stop'])

            if current_time < start:
                while current_time + 30 <= start:
                    self.free_windows.append({
                        'start': self._minutes_to_time(current_time),
                        'stop': self._minutes_to_time(current_time + 30),
                    })
                    current_time += 30

            current_time = stop

        if current_time < self._time_to_minutes(self.end_time):
            while current_time + 30 <= self._time_to_minutes(self.end_time):
                self.free_windows.append({
                    'start': self._minutes_to_time(current_time),
                    'stop': self._minutes_to_time(current_time + 30),
                })
                current_time += 30

        return self.free_windows

busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

doctor_worktime = WorkSchedule(busy)
print(doctor_worktime.get_daily_schedule())
