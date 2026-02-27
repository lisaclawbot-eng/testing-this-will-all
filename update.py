import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        task = " ".join(sys.argv[1:])
        # This line is the fix: Correctly format the HTML command to be injected.
        html_command = f'<script>appendToBody(\"{task}\");</script>'
        print(html_command)
    else:
        print("No task provided. Please provide a task to add to the dashboard.")