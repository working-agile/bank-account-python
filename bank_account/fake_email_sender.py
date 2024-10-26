class FakeEmailSender:
    def __init__(self):
        self.has_sent_email = False
        self.how_many_times_sent_email = 0

    def send_email_to_bank(self):
        print("Faking that I am sending the email to the bank administration")
        self.has_sent_email = True
        self.how_many_times_sent_email += 1
        