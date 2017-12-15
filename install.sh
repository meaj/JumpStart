#!/bin/sh

set -x

# check if being run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Installer must be run as root."
    exit
fi

SYSTEM_PREREQ="python3 python3-pip"
PYTHON_PREREQ="django==1.11"

OPT_DIR="/opt/jumpstart/"
VAR_DIR="/var/opt/jumpstart/"
ETC_DIR="/etc/opt/jumpstart/"
USER_NAME="jumpstart"

# test prerequisites
echo "Checking if required packages are installed..."
for pkg in "${SYSTEM_PREREQ}"
    do
        echo "Installing '$pkg'..."
        apt-get -y install $pkg
        if [ $? -ne 0 ]; then
            echo "Error installing system package '$pkg'"
            exit 1
        fi
    done

for ppkg in "${PYTHON_PREREQ}"
    do
        echo "Installing Python package '$ppkg'..."
        pip3 install $ppkg
        if [ $? -ne 0 ]; then
            echo "Error installing python package '$ppkg'"
            exit 1
        fi
done

echo "All required packages are installed."

set -e

echo "Copying app files to ${OPT_DIR}..."
mkdir -p ${OPT_DIR}
rm -rv ${OPT_DIR}*
cp -r ./source/* ${OPT_DIR}

echo "Creating ${VAR_DIR}..."
mkdir -p ${VAR_DIR}

echo "Creating ${ETC_DIR}..."
mkdir -p ${ETC_DIR}

grep "${USER_NAME}:" /etc/passwd
if [ $? -ne 0 ]; then
    echo "Creating system user ${USER_NAME}..."
    useradd --system --user-group --shell /bin/sh ${USER_NAME}
        if [ $? -ne 0 ]; then
            echo "Could not create system user."
            exit 1
        fi
fi

echo "Generating secret key..."
hexdump -n 64 -e '16 4 "%08X" 1 "\n"' /dev/random > ${ETC_DIR}secretKey.txt

echo "Setting ownership and permissions of application folders..."
chown --recursive ${USER_NAME}:${USER_NAME} ${OPT_DIR} ${VAR_DIR} ${ETC_DIR}
chmod --recursive a=,a=rX,ug+x ${OPT_DIR}
chmod --recursive a=,a=rX,ug+w ${VAR_DIR}
chmod --recursive a=,ug=rX ${ETC_DIR}

cp ./jumpstartinit.sh /etc/init.d/jumpstart
systemctl daemon-reload
service jumpstart start
