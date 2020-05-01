import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Hello Kubeflow World')
    parser.add_argument('--first',  type=str, help='The first text.', default="first arg")
    parser.add_argument('--second', type=str, help='The second text.', default="second arg")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print("First arg: {}, Second arg:{}".format(args.first, args.second))

