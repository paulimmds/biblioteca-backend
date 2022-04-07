from application import create_app

""" Options : development | production """
app = create_app('development')

if __name__ == "__main__":
    app.run()