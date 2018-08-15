##### WORKING
# create machine
```bash
aws ec2 run-instances --image-id ami-97785bed --instance-type t2.micro --count 1 --key-name bryan_mbr --security-group-ids sg-e66f1590
```
# ssh to machine
```bash
ssh -i $KAWS ec2-user@ec2-52-206-2-198.compute-1.amazonaws.com
```

# this will update yum, and install pip on amazon ami
```bash
sudo yum -y update
sudo yum -y install python36 python36-virtualenv python36-pip
```

# set up virtual python3 env
```bash
virtualenv -p python3 builder
source ./builder/bin/activate
pushd builder
```

# upgrade pip and install lxml
```bash
./bin/pip install --upgrade pip
./bin/pip install lxml==3.7.3
```

# navigate to lxml package and ZIP
```bash
pushd lib64/python3.6/site-packages/
zip -r9 lxml-3.7.3.amzn1.zip lxml lxml-3.7.3-py3.5.egg-info/
```

# scp file
```bash
scp -i $KAWS ec2-user@ec2-52-206-2-198.compute-1.amazonaws.com:./builder/lib64/python3.6/site-packages/lxml-3.7.3.amzn1.zip .
```

# terminate instance
```bash
aws ec2 terminate-instances --instance-id i-07b59e04fb55b95c4
```
