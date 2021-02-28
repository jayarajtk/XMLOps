from collections import OrderedDict

import xmltodict


def process_and_write(input_file):
    # Convert to dict
    with open(input_file, 'rb') as f:
        xml_content = xmltodict.parse(f)
    # print(xml_content)
    # Flatten dict
    flattened_xml = flatten_dict(xml_content)
    sorted_map = {k: v for k, v in sorted(flattened_xml.items(), key=lambda item: item[1])}
    # Print in desired format
    # for k, v in sorted_map.items():
    #     print('{} = {}'.format(v, k))
    with open(input_file.replace(".", "_") + "_flattened.txt", 'w') as file:
        for k, v in sorted_map.items():
            file.write('{} = {}\n'.format(v, k))
    return True


def flatten_dict(d):
    def items():
        for key, value in d.items():
            if isinstance(value, dict):
                for subKey, subValue in flatten_dict(value).items():
                    yield key + "." + subKey, subValue
            elif isinstance(value, list):
                index = 0
                for listItem in value:
                    for subKey, subValue in flatten_dict(listItem).items():
                        yield key + "[" + str(index) + "]." + subKey, subValue
                    index = index + 1
            else:
                yield key, value

    return OrderedDict(items())


process_and_write("test1.xml")
process_and_write("test2.xml")
