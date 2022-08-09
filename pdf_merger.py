import os
from PyPDF2 import PdfFileMerger


def merge_all_pdfs(path):
    """
    param path: path to directory with pdf documents
    return: None
    It's useful when all documents in the directory are single pages of only ONE document
    """
    merger = PdfFileMerger()

    for root, dirs, file_names in os.walk(path):
        file_names.sort()
        for fn in file_names:
            merger.append(path + fn)

    merger.write("Merged_pdfs_v1.pdf")
    merger.close()


def merge_groups_of_pdfs(path):
    """
    :param path: path to directory with pdf documents
    :return: None
    Function generates single (larger) pdfs from groups of single-paged pdf files
    """
    number_of_items_with_the_same_prefix = 0

    for root, dirs, file_names in os.walk(path):
        file_names.sort()

        # first we need to delete from temporary list elements
        # that don't have number after underscore in their name
        for i in range(len(file_names) - 1, -1, -1):
            if not check_if_number_after_underscore(file_names[i]):
                del file_names[i]

        for i in range(len(file_names) - 1):
            # create new instance of PdfFileMerger when needed
            if not number_of_items_with_the_same_prefix:
                merger = PdfFileMerger()

            if check_if_consecutive_number(
                file_names[i], file_names[i + 1]
            ) and check_if_consecutive_names(file_names[i], file_names[i + 1]):
                merger.append(path + file_names[i])  # add another page
                number_of_items_with_the_same_prefix += 1  # reset counter
            else:
                merger.append(path + file_names[i])
                merger.write(file_names[i].rsplit(".")[-2].rsplit("_", 1)[-2] + ".pdf")  # write pdf with right pages
                number_of_items_with_the_same_prefix = 0
                merger.close()

        # checking two last documents from the list of files
        if check_if_consecutive_number(
            file_names[-2], file_names[-1]
        ) and check_if_consecutive_names(file_names[-2], file_names[-1]):
            merger.append(path + file_names[-1])
            merger.write(file_names[-1].rsplit(".")[-2].rsplit("_", 1)[-2] + ".pdf")
            number_of_items_with_the_same_prefix = 0
            merger.close()

        else:  # if single document is at the end
            merger.close()
            number_of_items_with_the_same_prefix = 0
            merger = PdfFileMerger()
            merger.append(path + file_names[-1])
            merger.write(file_names[-1].rsplit(".")[-2].rsplit("_", 1)[-2] + ".pdf")
            merger.close()
    print("Finished merging pdfs!")


def check_if_consecutive_number(str1, str2):
    """
    :param str1: name of the first file
    :param str2: name of the second file
    :return: True if str2 has the same name as str1 (before "_")
             False otherwise
    """
    if (
        int(str1.rsplit(".")[-2].rsplit("_")[-1])
        == int(str2.rsplit(".")[-2].rsplit("_")[-1]) - 1
    ):
        return True
    else:
        return False


def check_if_consecutive_names(str1, str2):
    """
    :param str1: name of the first file
    :param str2: name of the second file
    :return: True if str2 has the number after "_" one more greater than from str1
             False otherwise
    """
    if (
        str1.rsplit(".")[-2].rsplit("_", 1)[-2]
        == str2.rsplit(".")[-2].rsplit("_", 1)[-2]
    ):
        return True
    else:
        return False


def check_if_number_after_underscore(file_name):
    """
    :param file_name: name of the file
    :return: True if file_name has a number after "_" in its name
             False otherwise
    """
    return file_name.rsplit(".")[-2].rsplit("_")[-1].isdigit()


if __name__ == "__main__":
    merge_groups_of_pdfs("pdfs/")
