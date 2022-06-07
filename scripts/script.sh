#!/bin/sh

set -e

echo "$(date): Ejecutando proceso"
cd /app
# sudo pkill python
python LimpiesaBot.py --windowed 
echo "$(date): Fin del proceso"
