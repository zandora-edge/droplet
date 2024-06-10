import json
import os
import shutil


def main():
    html = '<html><head><title>Droplet - URL Shortning Service</title><link rel="icon" href="dist/img/favicon.ico" type="image/x-icon"><meta http-equiv="refresh" content="0;url={url}" /></head><body><p>Redirecting...</p></body></html>'

    with open('links.json') as f:
        links = json.load(f)

    shutil.rmtree('dist', ignore_errors=True)
    os.mkdir('dist')

    with open('dist/CNAME', 'w') as f:
        f.write('drp.lt')

    for link in links:
        html_document = html.format(url=link['url'])
        file_path = f"dist/{link['name']}.html"

        with open(file_path, 'w') as f:
            f.write(html_document)


if __name__ == "__main__":
    main()
