#product_id = ['HEM-234','HEM-123','HEM-566']
#[234,123,566]

def main():
    product_id = ['HEM-234', 'HEM-123', 'HEM-566']
    output = [int(item.split('-')[1]) for item in product_id]
    print(output)
 
if __name__ == "__main__":
    main()