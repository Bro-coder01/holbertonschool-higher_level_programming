import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    if not isinstance(template, str):
        print(f"Error: Invalid template type. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid attendees type. Expected list of dictionaries, got {type(attendees).__name__}.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        processed_content = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None or str(value).strip() == "":
                value = "N/A"
            processed_content = processed_content.replace(f"{{{key}}}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(processed_content)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
