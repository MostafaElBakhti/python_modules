def secure_archive(filename, action="read", content="") -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
                return (True, data)

        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        return (False, "Invalid action")
    except Exception as error:
        return (False, str(error))
