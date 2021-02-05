from profile import Twitter


twitter_account = Twitter()

for s in twitter_account.get_sections():
    s.describe()
