class Test:

    def __init__(self):
        pass

    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')


t = Test()
with t:
    print('hello')
