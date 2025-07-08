#!/bin/bash
# Run the Quantum Crypto Cryptography GUI application with virtual environment support (Linux/macOS/Windows)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${BLUE}[LOG]${NC} $1"
}
warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}
error() {
    echo -e "${RED}[ERROR]${NC} $1"
}
success() {
    echo -e "${GREEN}[OK]${NC} $1"
}

# Robust OS detection
OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
IS_WINDOWS=0
case "$OS" in
    mingw*|cygwin*|msys*) IS_WINDOWS=1 ;;
    *) IS_WINDOWS=0 ;;
esac

# Function to deactivate venv and print message
function finish {
    if [ -n "$VIRTUAL_ENV" ]; then
        deactivate
        success "Virtual environment deactivated."
    fi
}
trap finish EXIT

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    error "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    log "Creating Python virtual environment in .venv..."
    python3 -m venv .venv || { error "Failed to create virtual environment."; exit 1; }
else
    success "Virtual environment found."
fi

# Activate the virtual environment
if [ $IS_WINDOWS -eq 0 ]; then
    source .venv/bin/activate
else
    if [ -f ".venv/Scripts/activate" ]; then
        .venv/Scripts/activate
    else
        error "Could not find Windows venv activation script."
        exit 1
    fi
fi

# Upgrade pip in the venv
log "Upgrading pip..."
pip install --upgrade pip

# Install required packages
log "Installing required Python packages..."
pip install -r requirements.txt || { error "Failed to install dependencies."; exit 1; }

# Run the application
log "Launching Quantum Crypto Cryptography GUI..."
python -m src.main 