from datetime import datetime


class History:

    @staticmethod
    def save(module, prompt):

        with open("logs/history.log", "a", encoding="utf-8") as f:

            f.write(
                f"{datetime.now()} | {module} | {prompt}\n"
            )