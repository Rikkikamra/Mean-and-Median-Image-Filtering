import sys


def apply_filter(img_matrix, filter_size,mode):
    filtered_matrix = img_matrix[:]
    height = len(img_matrix)
    width = len(img_matrix[0])
    filter = filter_size**2
    if(mode == "mean"):
        start = int(filter_size/2)
        sum = 0
        for i in range(start,height-start):
            for j in range(start,width-start):
                for k in range(-start,start+1):
                    for l in range(-start,start+1):
                        sum = sum+img_matrix[i+k][j+l]
                filtered_matrix[i][j] = (sum/filter)
                sum = 0

    elif(mode == "median"):
        filter_value = [0] * filter
        index = 0
        start = int(filter_size/2)
        mid = int(filter/2)
        for i in range(start,height-start):
            for j in range(start,width-start):
                for k in range(-start,start+1):
                    for l in range(-start,start+1):
                        filter_value[index] = img_matrix[i+k][j+l]
                        index +=1
                filter_value.sort()
                filtered_matrix[i][j] = filter_value[mid]
                index = 0
        
    return filtered_matrix

def read_ppm(input):
    with open(input, 'r') as f:
        magic_number = f.readline()
        comment = f.readline()
        size = f.readline().split()
        max_val = f.readline()
        width, height = int(size[0]), int(size[1])
        img_matrix = [[0 for j in range(width)] for i in range(height)]
        for i in range(height):
            pixel_row = f.readline().split()
            for j, pixel in enumerate(pixel_row):
                img_matrix[i][j] = int(pixel)
        return img_matrix


def write_ppm(output, img_matrix):
    width = len(img_matrix[0])
    height = len(img_matrix)
    with open(output, 'w') as fw:
        fw.write('P2\n')
        fw.write(
            '# Image from: https://homepages.inf.ed.ac.uk/rbf/HIPR2/median.htm\n'
        )
        fw.write('%d %d\n' % (width, height))
        fw.write('255\n')
        for img_row in img_matrix:
            for pixel in img_row:
                fw.write('%d ' % pixel)
            fw.write('\n')


def main():
    if len(sys.argv) < 4:
        print('Usage: python %s <input_file> <output_file> <filter_size> <mean/median>' %
              sys.argv[0])
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    filter_size = int(sys.argv[3])
    mode = sys.argv[4]
    img_matrix = read_ppm(input_file)
    flt_matrix = apply_filter(img_matrix, filter_size,mode)
    write_ppm(output_file, flt_matrix)


if __name__ == '__main__':
    main()
