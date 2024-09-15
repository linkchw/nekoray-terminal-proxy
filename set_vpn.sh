#!/bin/bash

set_temp_proxy() {
  export http_proxy=192.168.88.111:10809
  echo "Temporary proxy added."
}

set_perm_proxy() {
  echo "Adding proxy to .bashrc and .zshrc..."
  
  echo "export http_proxy=192.168.88.111:10809" >> ~/.bashrc
  echo "Permanent proxy added to .bashrc."
  
  if [ -f ~/.zshrc ]; then
    echo "export http_proxy=192.168.88.111:10809" >> ~/.zshrc
    echo "Permanent proxy added to .zshrc."
  else
    echo ".zshrc not found, skipping."
  fi
  
  echo "Please restart your terminal or run 'source ~/.bashrc' and 'source ~/.zshrc' to apply changes."
  
  read -p "Do you want to remove the proxy lines from .bashrc and .zshrc? (y/n): " remove_choice
  if [[ $remove_choice == "y" ]]; then
    sed -i '/export http_proxy=192.168.88.111:10809/d' ~/.bashrc
    echo "Removed proxy from .bashrc."
    
    if [ -f ~/.zshrc ]; then
      sed -i '/export http_proxy=192.168.88.111:10809/d' ~/.zshrc
      echo "Removed proxy from .zshrc."
    fi
  fi
}

echo "Choose an option:"
echo "1) Set proxy temporarily"
echo "2) Set proxy permanently (add to .bashrc and .zshrc)"

read -p "Enter your choice (1 or 2): " choice

case $choice in
  1)
    set_temp_proxy
    ;;
  
  2)
    set_perm_proxy
    ;;
  
  *)
    echo "Invalid choice. Please enter 1 or 2."
    ;;
esac
