##### WORKING
```bash
# create machine
INSTANCEID=$(aws ec2 run-instances --image-id ami-1853ac65 --instance-type t2.micro --count 1 --key-name bryan_mbr --security-group-ids sg-e66f1590 | jq -r '.Instances[0].InstanceId')

# use describe-instances to get public dns name
DNSNAME=$(aws ec2 describe-instances --instance-id $INSTANCEID | jq -r '.Reservations[0].Instances[0].PublicDnsName')

# ssh to machine
ssh -i $KAWS ec2-user@$DNSNAME
```

# this will update yum, and install pip on amazon ami
```bash
sudo yum -y update
sudo yum -y install python36 python36-virtualenv python36-pip

# set up virtual python3 env
virtualenv -p python3 builder
source ./builder/bin/activate
pushd builder

# upgrade pip and install lxml
sudo yum install -y gcc libxml2 libxml2-devel libxslt libxslt-devel
./bin/pip install --upgrade pip
./bin/pip install lxml==4.2.5

# navigate to lxml package and ZIP
pushd lib64/python3.6/site-packages/
zip -r9 lxml-4.2.5.amzn1.zip lxml lxml-4.2.5.dist-info/
```

# scp file
```bash
scp -i $KAWS ec2-user@$DNSNAME:./builder/lib64/python3.6/site-packages/lxml-4.2.5.amzn1.zip .
```

# terminate instance
```bash
aws ec2 terminate-instances --instance-id $INSTANCEID
```
