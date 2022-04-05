from application import init_app

""" Options : development | production """
app = init_app('development')

if __name__ == "__main__":
    app.run()