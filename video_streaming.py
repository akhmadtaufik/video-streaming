# import library
from tabulate import tabulate

import string
import random

# tinggal di run saja
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"],
}


class PlanError(Exception):
    pass


# isilah titik - titik di bawah ini
class User:
    # database PacFlix
    data = {
        "Shandy": ["Basic Plan", 12, "shandy-2134"],
        "Cahya": ["Standard Plan", 24, "cahya-abcd"],
        "Ana": ["Premium Plan", 5, "ana-2f9g"],
        "Bagus": ["Basic Plan", 11, "bagus-9f92"],
    }

    # Create all benefit into class attribute
    benefit = [
        ["Basic Plan", "Standard Plan", "Premium Plan", "Services"],
        [True, True, True, "can_stream"],
        [True, True, True, "can_download"],
        [True, True, True, "has_SD"],
        [False, True, True, "has_HD"],
        [False, False, True, "has_UHD"],
        [1, 2, 4, "num_of_device"],
        [
            "3rd party movie only",
            "Basic Plan Content + Sports\n(F1, Football, Basketball)",
            "Basic Plan + Standard Plan +\nPacFlix Original Series or Movie",
            "content",
        ],
        [120000, 160000, 200000, "price"],
    ]

    def __init__(self, username: str, duration_plan: int, current_plan: str):
        """_summary_

        Args:
            username (str): _description_
            duration_plan (int): _description_
            current_plan (str): _description_

        Raises:
            TypeError: _description_
            TypeError: _description_
            TypeError: _description_
            NameError: _description_

        Returns:
            _type_: _description_
        """

        try:
            # Check type of data from all parameter
            if type(username) != str:
                raise TypeError("Tipe data 'username' harus str")

            elif type(duration_plan) != int:
                raise TypeError("Tipe data 'duration_plan' harus int")

            elif type(current_plan) != str:
                raise TypeError("Tipe data 'current_plan' harus str")

            else:
                # Initiate attribute
                self.username = username
                self.duration_plan = duration_plan
                self.current_plan = current_plan

                # Check username in database
                if username in self.data.keys():
                    return None
                else:
                    raise NameError

        except NameError:
            print("Username tidak ditemukan, silahkan sign-up di PacFlix")

    def check_benefit(self):
        """Function to show all benefit in PacFlix

        Returns:
            table: table of all benefit in PacFilx
        """

        print("PacFlix Plan List\n")

        # Assign all benefit into table
        table = tabulate(self.benefit, headers="firstrow")

        return print(table)

    def check_plan(self, username: str):
        """_summary_

        Args:
            username (str): _description_

        Raises:
            TypeError: _description_
            NameError: _description_
        """

        try:
            if type(username) != str:
                raise TypeError("Tipe data 'username' harus str")

            else:
                # Check username in database
                if username in self.data.keys():
                    print(self.data[username][0])
                    print(f"{self.data[username][1]} Bulan")
                    print("\n")
                    print(f"{self.data[username][0]} PacFlix Benefit List\n")

                    # Filter current_benefit based on username
                    current_benefit = [
                        [index[0], index[3]] for index in self.benefit
                    ]

                    # Assign current benefit into table
                    table = tabulate(current_benefit, headers="firstrow")

                    print(table)
                    print("\n")
                    print(f"Code referral : {self.data[username][-1]}")

                else:
                    raise NameError

        except NameError:
            print("Username tidak ditemukan, silahkan sign-up di PacFlix")

    def upgrade_plan(self, username: str, current_plan: str, new_plan: str):
        """_summary_

        Args:
            username (str): _description_
            current_plan (str): _description_
            new_plan (str): _description_

        Raises:
            TypeError: _description_
            TypeError: _description_
            TypeError: _description_
            PlanError: _description_
            PlanError: _description_

        Returns:
            _type_: _description_
        """

        try:
            # Check type of data from all parameter
            if type(username) != str:
                raise TypeError("Tipe data 'username' harus str")

            elif type(current_plan) != str:
                raise TypeError("Tipe data 'current_plan' harus str")

            elif type(new_plan) != str:
                raise TypeError("Tipe data 'new_plan' harus str")

            else:
                # Check hierarcy new_plan and current_plan
                # User can't downgrade plan
                if self.benefit[0][:3].index(new_plan) < self.benefit[0][
                    :3
                ].index(current_plan):
                    raise PlanError("Tidak boleh downgrade plan")

                # Check new_plan and current_plan #
                # if return same value raise error
                elif new_plan == current_plan:
                    raise PlanError(
                        "'new_plan' dan 'current_plan' tidak boleh sama"
                    )

                # if new_plan and current_plan not same, execute
                else:
                    # Check username in database
                    if username in self.data.keys():
                        # Insert new_plan into database
                        self.data[username].insert(0, new_plan)
                        # Remove current_plan from database
                        self.data[username].pop(1)

                        # Check duration_plan based on username
                        # if duration_plan > 12 got 5% discount
                        if self.data[username][1] > 12:
                            # Check index price from database
                            index = self.benefit[0][:3].index(current_plan)
                            # Apply discount price based on new_plan
                            price = self.benefit[-1][index] * 0.95

                            return print(price)

                        # if duration_plan < 12 got normal price
                        else:
                            # Check index price from database
                            index = self.benefit[0][:3].index(current_plan)
                            # Return normal price based on new_plan
                            price = self.benefit[-1][index]

                            return print(price)

                    else:
                        return NameError

        except NameError:
            print("Username tidak ditemukan, silahkan sign-up di PacFlix")

        except ValueError:
            print(f"Plan {new_plan} tidak tersedia")


# isi titik - titik di bawah ini
class NewUser:

    ref_data = []

    data = {}

    # Create all benefit into class attribute
    benefit = [
        ["Basic Plan", "Standard Plan", "Premium Plan", "Services"],
        [True, True, True, "can_stream"],
        [True, True, True, "can_download"],
        [True, True, True, "has_SD"],
        [False, True, True, "has_HD"],
        [False, False, True, "has_UHD"],
        [1, 2, 4, "num_of_device"],
        [
            "3rd party movie only",
            "Basic Plan Content + Sports\n(F1, Football, Basketball)",
            "Basic Plan + Standard Plan +\nPacFlix Original Series or Movie",
            "content",
        ],
        [120000, 160000, 200000, "price"],
    ]

    def __init__(self, username):
        """_summary_

        Args:
            username (_type_): _description_
        """

        self.username = username

    def check_benefit(self):
        """Function to show all benefit in PacFlix

        Returns:
            table: table of all benefit in PacFilx
        """

        print("PacFlix Plan List\n")

        # Assign all benefit into table
        table = tabulate(self.benefit, headers="firstrow", tablefmt="github")

        return print(table)

    def convert_data_to_list(self, data):
        """_summary_

        Args:
            data (_type_): _description_
        """

        for ref in data.values():
            self.ref_data.append(ref[-1])

    def pick_plan(self, new_plan, referral_code):
        """_summary_

        Args:
            new_plan (_type_): _description_
            referral_code (_type_): _description_

        Raises:
            PlanError: _description_
            ValueError: _description_
            KeyError: _description_

        Returns:
            _type_: _description_
        """

        # initializing size of string
        N = 4
        # using random.choices()
        # generating random strings
        res = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=N)
        )

        if self.username not in self.data.keys():
            if referral_code in self.ref_data:
                if new_plan == "Basic Plan":
                    self.data[self.username] = [
                        self.benefit[0][0],
                        0,
                        f"{self.username.lower()}-{str(res)}",
                    ]
                    price = self.benefit[-1][0] * 0.96
                    return print(price)

                elif new_plan == "Standard Plan":
                    self.data[self.username] = [
                        self.benefit[0][1],
                        0,
                        f"{self.username.lower()}-{str(res)}",
                    ]
                    price = self.benefit[-1][1] * 0.96
                    return print(price)

                elif new_plan == "Premium Plan":
                    self.data[self.username] = [
                        self.benefit[0][2],
                        0,
                        f"{self.username.lower()}-{str(res)}",
                    ]
                    price = self.benefit[-1][2] * 0.96
                    return print(price)

                else:
                    raise PlanError("Plan doesn't exist")

            else:
                raise ValueError("Referral code doesn't exist")

        else:
            raise KeyError("Username exist")
