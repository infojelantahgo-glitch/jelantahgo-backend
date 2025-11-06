#!/bin/bash
# Deployment script for VPS
# Usage: ./deploy.sh

set -e

echo "🚀 Starting deployment..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Install/update dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

# Run database migrations (if using Alembic)
# alembic upgrade head

# Initialize database if needed
echo -e "${YELLOW}Initializing database...${NC}"
python init_db.py || echo "Database already initialized"

# Create uploads directory if it doesn't exist
mkdir -p uploads/payment_proofs

# Restart application (using systemd, PM2, or supervisor)
echo -e "${GREEN}Deployment complete!${NC}"
echo -e "${YELLOW}Restart your application service:${NC}"
echo "  systemctl restart jelantahgo-backend"
echo "  # or"
echo "  pm2 restart jelantahgo-backend"
echo "  # or"
echo "  supervisorctl restart jelantahgo-backend"

