#Zandora Edge Pvt. Ltd.
import json
import os
import shutil

def main():
    html = '<html><head><title>Droplet - URL Shortening Service</title><link rel="icon" href="dist/img/favicon.ico" type="image/x-icon"><meta http-equiv="refresh" content="0;url={url}" /></head><body><p>Redirecting...</p></body></html>'

    with open('links.json') as f:
        links = json.load(f)

    # Exclude these files from deletion
    exclude_files = ['example.html']

    # Remove files in 'dist' directory except for the excluded files
    if os.path.exists('dist'):
        for item in os.listdir('dist'):
            item_path = os.path.join('dist', item)
            if item not in exclude_files:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)

    os.makedirs('dist', exist_ok=True)

    with open('dist/CNAME', 'w') as f:
        f.write('drp.lt')

    for link in links:
        html_document = html.format(url=link['url'])
        file_path = f"dist/{link['name']}.html"

        with open(file_path, 'w') as f:
            f.write(html_document)

if __name__ == "__main__":
    main()
