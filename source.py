def exists(path, proxy_line):
    with open(path, 'r') as file:
        line = file.readlines()
        
        flag = False
        for i in line:
            if proxy_line in i:
                flag = True
                break
            else: 
                flag = False
            
    file.close()
    return flag
    

def deactivate(path, proxy_line):
    with open(path, 'r+') as file:
        line = file.readlines()
        final_file = [i for i in line]

        if exists(path, proxy_line): 
            for i in final_file:
                if proxy_line in i:
                    del final_file[final_file.index(i)]
                    final_file.append(f"#{proxy_line}")
                    print("proxy has been DEACTIVATED successfully!")

            file.truncate(0)
            file.seek(0)
            file.writelines(final_file)
        else:
            print("Proxy Config not found! disabled config added")
            final_file.append(f"\n#{proxy_line}")
            file.truncate(0)
            file.seek(0)
            file.writelines(final_file)

    file.close()


def activate(path, proxy_line):
    with open(path, 'r+') as file:
        line = file.readlines()
        final_file = [i for i in line]

        if exists(path, proxy_line): 
            for i in final_file:
                if proxy_line in i:
                    del final_file[final_file.index(i)]
                    final_file.append(proxy_line)
                    print("proxy has been ACTIVATED successfully!")

            file.truncate(0)
            file.seek(0)
            file.writelines(final_file)
        else:
            print("Proxy Config not found! activated config added")
            final_file.append("\n" + proxy_line)
            file.truncate(0)
            file.seek(0)
            file.writelines(final_file)

    file.close()


def main():
    file_path = "/etc/environment"
    proxy = "export http_proxy=\"http://127.0.0.1:2081/\""
    
    user_input = input("[a]ctivate, [d]isable: ").strip().lower()
    if user_input == 'a':
        activate(file_path, proxy)

    elif user_input == 'd':
        deactivate(file_path, proxy)
    else: 
        print('Not an option!')


if __name__ == "__main__":
    main()
