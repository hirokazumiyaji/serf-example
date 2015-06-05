# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
sudo apt-get install -y unzip
sudo locale-gen ja_JP.UTF-8

echo Fetching Serf...
cd /tmp
wget https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip -O serf.zip

echo Installing Serf...
unzip serf.zip
sudo chmod +x serf
sudo mv serf /usr/bin/serf
SCRIPT

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.provision "shell", inline: $script

  config.vm.define "node1" do |node|
    node.vm.network "private_network", ip: "172.20.20.10"
  end

  config.vm.define "node2" do |node|
    node.vm.network "private_network", ip: "172.20.20.11"
  end

end
