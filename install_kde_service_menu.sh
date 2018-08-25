#!/bin/bash

SERVICE_MENUS_DIR=~/.local/share/kservices5/ServiceMenus
MIME_DIR=~/.local/share/mime/user-extension
EXEC=CiaServer.py
DESKTOP_FILE="Install CIA from QRCode.desktop"
MIME_FILE="x.3ds-cia.xml"
SRC_DIR=$(cd "$(dirname "$0")"; pwd)


mkdir -p "$SERVICE_MENUS_DIR"
cp "$DESKTOP_FILE" "$SERVICE_MENUS_DIR"
sed -i -- "s|{EXEC}|$SRC_DIR/CiaServer.py|g" "$SERVICE_MENUS_DIR/$DESKTOP_FILE"

mkdir -p "$MIME_DIR"
cp "$MIME_FILE" "$MIME_DIR"

chmod +X "$SRC_DIR/$EXEC"
