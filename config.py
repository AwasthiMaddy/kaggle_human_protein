class DefaultConfigs(object):
    train_data = "/home/femi/work/datasets/HumanProtein/train/" # where is your train data
    test_data = "/home/femi/work/datasets/HumanProtein/test/"   # your test data
    external_data = "/home/femi/work/datasets/HumanProtein/external_data_HPAv18/"
    test_csv = "/home/femi/work/datasets/HumanProtein/sample_submission.csv"
    train_csv = "/home/femi/work/datasets/HumanProtein/train.csv"
    external_csv = "/home/femi/work/datasets/HumanProtein/external_data_HPAv18.csv"
    test_matches_csv = "/home/femi/work/datasets/HumanProtein/test_matches.csv"
    weights = "./checkpoints/"
    best_models = "./checkpoints/best_models/"
    submit = "./submit/"
    model_name = "densenet121"
    num_classes = 28
    img_weight = 512
    img_height = 512
    channels = 4
    lr = 0.03
    batch_size = 8
    epochs = 24
    threshold = 0.15
    multiply = 1.3  # when weighted sampler  sample_num / raw_data_num
    min_sampling_limit = 0.5  # the min limit of log class weight
    fold = 12  # for me the 0,1 is test, and fold=2 is the start
    kfold_index = (fold - 2) % 5 + 1 # 2
    threshold_factor = [0.3, 0.4, 0.5]
    best = "f1"  # best_f1 or best_loss to switch for test
    is_train = True
    is_train_after_crash = False
    is_test = False
    is_search_thres = False
    tta = True
    opt_thres = True

config = DefaultConfigs()
