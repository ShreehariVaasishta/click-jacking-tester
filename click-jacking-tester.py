import contextlib
from urllib.request import urlopen
from urllib.parse import urlparse
from sys import argv, exit

from rich import print


def check(url):
    """check given URL is vulnerable or not"""
    url = url.replace("\n", "").strip()
    with contextlib.suppress(Exception):
        if "http" not in url:
            url = f"https://{url}"
        data = urlopen(url)
        domain = urlparse(url).netloc
        headers = data.info()
        if "X-Frame-Options" not in headers:
            print(f"\t\t[bold red]Website {domain} is vulnerable! :vampire:")
            create_poc(url)
            return True
    print("\t\t [green]Website is not vulnerable! \u2713")
    return False


def create_poc(url):
    """create HTML page of given URL"""
    code = """
<html>
   <head><title>Clickjack test page</title></head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="{}" width="100%" height="100%"></iframe>
   </body>
</html>
    """.format(
        url
    )
    domain = urlparse(url).netloc
    file_path = f"{domain}.html"
    with open(file_path, "w") as f:
        f.write(code)
        f.close()
    print(f"\t\tCreated a poc and saved to [link]{file_path}")


def main():
    """Everything comes together"""
    try:
        sites = open(argv[1], "r").readlines()
    except Exception:
        print("[bold red] Usage: python(3) clickjacking_tester.py <file_name>")
        exit(0)

    for site in sites:
        print(f"\n[bold green]Testing Site - {site}", end="")
        check(site)


if __name__ == "__main__":
    main()
