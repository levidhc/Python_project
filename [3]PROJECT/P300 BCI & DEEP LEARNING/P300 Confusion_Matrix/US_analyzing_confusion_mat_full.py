import numpy as np
import pandas as pd

for isub in range(30,60):
    confusion_matrix = np.zeros((2,2))

    for repeat_num in range(1,11):
        filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'RUS/CNN_fullch_rus_t' + str(repeat_num) + '_confusion_' + str(isub + 1) + '.csv'

        data = pd.read_csv(filename, header=0, index_col=0)
        data_np = np.array(data)

        confusion_matrix = confusion_matrix + data_np
        del data, data_np

    mean_confusion_matrix = confusion_matrix / 10

    df1 = pd.DataFrame(confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'RUS/CNN_fullch_rus_total_confusion_' + str(isub + 1) + '.csv'
    df1.to_csv(filename)

    df2 = pd.DataFrame(mean_confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'RUS/CNN_fullch_rus_mean_confusion_' + str(isub + 1) + '.csv'
    df2.to_csv(filename)

for isub in range(14):
    confusion_matrix = np.zeros((2,2))

    for repeat_num in range(1,11):
        filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'RUS/CNN_BS_fullch_rus_t' + str(repeat_num) + '_confusion_' + str(isub + 1) + '.csv'

        data = pd.read_csv(filename, header=0, index_col=0)
        data_np = np.array(data)

        confusion_matrix = confusion_matrix + data_np
        del data, data_np

    mean_confusion_matrix = confusion_matrix / 10

    df1 = pd.DataFrame(confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'RUS/CNN_BS_fullch_rus_total_confusion_' + str(isub + 1) + '.csv'
    df1.to_csv(filename)

    df2 = pd.DataFrame(mean_confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'RUS/CNN_BS_fullch_rus_mean_confusion_' + str(isub + 1) + '.csv'
    df2.to_csv(filename)

for isub in range(30,60):
    confusion_matrix = np.zeros((2,2))

    for repeat_num in range(1,11):
        filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'NCR/CNN_fullch_ncr_t' + str(repeat_num) + '_confusion_' + str(isub + 1) + '.csv'

        data = pd.read_csv(filename, header=0, index_col=0)
        data_np = np.array(data)

        confusion_matrix = confusion_matrix + data_np
        del data, data_np

    mean_confusion_matrix = confusion_matrix / 10

    df1 = pd.DataFrame(confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'NCR/CNN_fullch_ncr_total_confusion_' + str(isub + 1) + '.csv'
    df1.to_csv(filename)

    df2 = pd.DataFrame(mean_confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'NCR/CNN_fullch_ncr_mean_confusion_' + str(isub + 1) + '.csv'
    df2.to_csv(filename)

for isub in range(14):
    confusion_matrix = np.zeros((2,2))

    for repeat_num in range(1,11):
        filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'NCR/CNN_BS_fullch_ncr_t' + str(repeat_num) + '_confusion_' + str(isub + 1) + '.csv'

        data = pd.read_csv(filename, header=0, index_col=0)
        data_np = np.array(data)

        confusion_matrix = confusion_matrix + data_np
        del data, data_np

    mean_confusion_matrix = confusion_matrix / 10

    df1 = pd.DataFrame(confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'NCR/CNN_BS_fullch_ncr_total_confusion_' + str(isub + 1) + '.csv'
    df1.to_csv(filename)

    df2 = pd.DataFrame(mean_confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'NCR/CNN_BS_fullch_ncr_mean_confusion_' + str(isub + 1) + '.csv'
    df2.to_csv(filename)

for isub in range(30,60):
    confusion_matrix = np.zeros((2,2))

    for repeat_num in range(1,11):
        filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'Tomek/CNN_fullch_tomek_t' + str(repeat_num) + '_confusion_' + str(isub + 1) + '.csv'

        data = pd.read_csv(filename, header=0, index_col=0)
        data_np = np.array(data)

        confusion_matrix = confusion_matrix + data_np
        del data, data_np

    mean_confusion_matrix = confusion_matrix / 10

    df1 = pd.DataFrame(confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'Tomek/CNN_fullch_tomek_total_confusion_' + str(isub + 1) + '.csv'
    df1.to_csv(filename)

    df2 = pd.DataFrame(mean_confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'Tomek/CNN_fullch_tomek_mean_confusion_' + str(isub + 1) + '.csv'
    df2.to_csv(filename)

for isub in range(14):
    confusion_matrix = np.zeros((2,2))

    for repeat_num in range(1,11):
        filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'Tomek/CNN_BS_fullch_tomek_t' + str(repeat_num) + '_confusion_' + str(isub + 1) + '.csv'

        data = pd.read_csv(filename, header=0, index_col=0)
        data_np = np.array(data)

        confusion_matrix = confusion_matrix + data_np
        del data, data_np

    mean_confusion_matrix = confusion_matrix / 10

    df1 = pd.DataFrame(confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'Tomek/CNN_BS_fullch_tomek_total_confusion_' + str(isub + 1) + '.csv'
    df1.to_csv(filename)

    df2 = pd.DataFrame(mean_confusion_matrix)
    filename = 'C:/Users/jhpark/Documents/GitHub/Python_project/[3]PROJECT/P300 BCI & DEEP LEARNING/P300_sampling/UnderSampling/result/CONFUSION/' \
                   'Tomek/CNN_BS_fullch_tomek_mean_confusion_' + str(isub + 1) + '.csv'
    df2.to_csv(filename)