
class Log:
    def __init__(self, name):
            self.current_user = name
            self.categories = {
                "home": [],
                "subscriptions": [],
                "social": [],
                "etc": []
            }
            self.categoryName = "etc"

    def add_history(self, categoryno, history):
            categories = {
                    1: "home",
                    2: "subscriptions",
                    3: "social",
                    4: "etc"
            }

            self.categoryName = categories.get(categoryno)
            self.categories[self.categoryName].append(history)

    def check_history(self):
            print(self.categories)
        



    