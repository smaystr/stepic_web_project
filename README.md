# stepic_web_project

mkdir -p ~/web && \
cd ~/web && \
git clone https://github.com/smaystr/stepic_web_project.git ~/web && \
sudo ./init.sh \
sudo chmod -R a+rw ~/web

if git files changed locally, stash or reset:
git reset --hard
