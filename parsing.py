import re

# @input: log filename
# @return: a list of 4 lists in the format of
#		[[train loss 1, train loss 2, train loss 3 ...]
#		 [val loss 1, val loss 2, val loss 3 ...]
#		 [test loss 1, test loss 2, test loss 3 ...]
#        [best_epoch_pos]
#        ]

def read_log(file):
    train_pattern = re.compile('^Train set:')
    val_pattern = re.compile('^Validation set:')
    test_pattern = re.compile('^Test set:')
    loss_pattern = re.compile('loss: (\d*\.)?\d+')
    with open(file, 'r') as log:
        train, val, test = [], [], []
        best_validation_loss = 1.0
        for line in log:
            if train_pattern.match(line):
                train.append(float(re.sub('[^\d.]','',(loss_pattern.search(line).group(0)))))
            if val_pattern.match(line):
                validation_loss = float(re.sub('[^\d.]', '', loss_pattern.search(line).group(0)))
                val.append(validation_loss)
                if validation_loss < best_validation_loss:
                    best_validation_loss = validation_loss
                    best_epoch = len(val)
            if test_pattern.match(line):
                test.append(float(re.sub('[^\d.]', '', loss_pattern.search(line).group(0))))
        return [train, val, test, [best_epoch]]
