#ZanX Technologies a division of Zandora Edge Pvt. Ltd.
import json
import os
import shutil

def main():
    html = '<html><head><title>Droplet - URL Shortening Service</title><link rel="icon" href="dist/img/favicon.ico" type="image/x-icon"><meta http-equiv="refresh" content="0;url={url}" /></head><body><p>Redirecting...</p></body></html>'

    with open('links.json') as f:
        links = json.load(f)

    # List of files and directories to preserve
    preserve = ['example.html']

    # Create missing directory if needed
    if not os.path.exists('dist'):
        os.mkdir('dist')

    # Delete only files and directories not in the preserve list
    for item in os.listdir('dist'):
        if item not in preserve:
            item_path = os.path.join('dist', item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

    with open('dist/CNAME', 'w') as f:
        f.write('drp.lt')

    for link in links:
        html_document = html.format(url=link['url'])
        file_path = f"dist/{link['name']}.html"

        with open(file_path, 'w') as f:
            f.write(html_document)

if __name__ == "__main__":
    main()
