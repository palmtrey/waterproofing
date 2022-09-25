import json

def minimum(json_file: str):
    with open(json_file, 'r') as f:
        l = json.load(f)
    
    return min(l.items(), key=lambda x: x[1])


if __name__ == '__main__':
    print(minimum('depth_offset_factor_results.txt'))
