# flake8: noqa
import os.path as osp

import hat.archs
import hat.data
import hat.models
from basicsr.export import export_model

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    export_model(root_path)
