import argparse
import urllib.parse

parser = argparse.ArgumentParser(description='URL encoder and decoder')
parser.add_argument('-u', '--url', type=str, help='URL to encode or decode. Should be enclosed in double quotes.')
parser.add_argument('-e', '--encode', action='store_true', help='Encode the URL')
parser.add_argument('-d', '--decode', action='store_true', help='Decode the URL')
parser.add_argument('-n', type=int, default=1, choices=[1, 2, 3], help='Number of times to encode or decode the URL (1, 2, or 3)')
parser.add_argument('-f', '--full', action='store_true', help='Encode the full URL including the prefix')

args = parser.parse_args()

if args.url:
    if args.full:
        encoded_url = args.url
        for _ in range(args.n):
            encoded_url = urllib.parse.quote(encoded_url)
        print(f'\nEncoded Full URL ({args.n} times): {encoded_url}')
    elif args.encode:
        if args.url.startswith("http://") or args.url.startswith("https://"):
            base_url = args.url.split('://')[0] + '://' + args.url.split('://')[1].split('/')[0]
            path = '/' + '/'.join(args.url.split('://')[1].split('/')[1:])
        else:
            base_url = ""
            path = args.url
        encoded_path = path
        for _ in range(args.n):
            encoded_path = urllib.parse.quote(encoded_path)
        encoded_url = base_url + encoded_path
        print(f'\nEncoded URL ({args.n} times): {encoded_url}')
    elif args.decode:
        decoded_url = args.url
        for _ in range(args.n):
            decoded_url = urllib.parse.unquote(decoded_url)
        print(f'\nDecoded URL ({args.n} times): {decoded_url}')
    else:
        print('Please specify whether to encode (-e) or decode (-d) the URL.')
else:
    print('Please provide a URL using -u or --url argument. For help using -h')

