from io import StringIO
import csv
import ics
from datetime import datetime

def generate_ics_from_csv(csv_data):
    """
    Converts CSV data to an ICS calendar file content.

    Args:
        csv_data (str): The CSV data as a string.

    Returns:
        str: The content of the ICS calendar file.
    """
    try:
        csv_file = StringIO(csv_data)
        reader = csv.reader(csv_file, delimiter=";")
        next(reader)  # Skip header row

        calendar = ics.Calendar()

        for row in reader:
            sched_date, activity, start_time, end_time, _ = row

            # Format start and end times
            start_time = f"{start_time}:00" if len(start_time.split(':')) == 2 else start_time
            end_time = f"{end_time}:00" if len(end_time.split(':')) == 2 else end_time

            try:
                start_datetime = datetime.strptime(f"{sched_date} {start_time}", '%Y-%m-%d %H:%M:%S')
                end_datetime = datetime.strptime(f"{sched_date} {end_time}", '%Y-%m-%d %H:%M:%S')

                # Create an event and add it to the calendar
                event = ics.Event(
                    name=activity,
                    begin=start_datetime,
                    end=end_datetime
                )
                calendar.events.add(event)

            except ValueError as e:
                print(f"Error parsing date/time: {e}")
                print(f"Row data: {row}")  # Print problematic row for debugging

        # Return the calendar as a string
        return str(calendar)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Indicate failure by returning None
