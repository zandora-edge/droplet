#Zandora Edge Pvt. Ltd.
import json
import os
import shutil


def clear_dist_except(exceptions):
    for item in os.listdir('dist'):
        print(item)
        item_path = os.path.join('dist', item)
        if item not in exceptions:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)


def main():
    html = '<html><head><title>Droplet - URL Shortning Service</title><link rel="icon" href="dist/img/favicon.ico" type="image/x-icon"><meta http-equiv="refresh" content="0;url={url}" /></head><body><p>Redirecting...</p></body></html>'

    with open('links.json') as f:
        links = json.load(f)

    # Create 'dist' directory if it doesn't exist
    if not os.path.exists('dist'):
        os.mkdir('dist')

    # Clear 'dist' directory except specified exceptions
    exceptions = ['example.html']  # Add the subfolders you want to keep here
    clear_dist_except(exceptions)

    # Create or overwrite the CNAME file
    with open('dist/CNAME', 'w') as f:
        f.write('drp.lt')

    # Create or overwrite the redirect files
    for link in links:
        html_document = html.format(url=link['url'])
        file_path = f"dist/{link['name']}.html"

        with open(file_path, 'w') as f:
            f.write(html_document)


if __name__ == "__main__":
    main()

