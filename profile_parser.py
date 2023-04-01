def get_server_address_and_port_from_profile(file_path):
    server_address = None
    server_port = None
    with open(file_path, 'r') as f:
        for line in f.readlines():
            if line.startswith('remote '):
                tokens = line.split()
                server_address = tokens[1]
                if len(tokens) > 2:
                    server_port = int(tokens[2])
                break
    return server_address, server_port
