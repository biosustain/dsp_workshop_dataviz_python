# the yarn apt repo shipped with the base image has an expired GPG key, which makes `apt update` fail
sudo rm -f /etc/apt/sources.list.d/yarn.list
sudo apt update && sudo apt-get -y install libnss3 libdbus-1-3 libatk1.0-0 libatspi2.0-0 libatk-bridge2.0-0 libcups2 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libxkbcommon0 libpango-1.0-0 libcairo2 libasound2
pip3 install --user -r requirements.txt
kaleido_get_chrome
