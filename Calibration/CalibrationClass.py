import cv2
import numpy as np
import os
import glob

class CalibrateImage:
    def __init__(self):
        self.checkerboard = (6,9)
        self.criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        self.objpoints = []
        self.imgpoints = []
        self.prev_img_shape = None

    def Calibrate(self):
        objp = np.zeros((1, self.checkerboard[0] * self.checkerboard[1], 3), np.float32)
        objp[0,:,:2] = np.mgrid[0:self.checkerboard[0], 0:self.checkerboard[1]].T.reshape(-1, 2)
        
        images = glob.glob('./images/*.jpg')
        for fname in images:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(gray, 
                                                     self.checkerboard,
                                                     cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
            
            if ret == True:
                self.objpoints.append(objp)
                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
                self.imgpoints.append(corners2)
                img = cv2.drawChessboardCorners(img, self.checkerboard, corners2, ret)
            
            cv2.imshow('img', img)
            cv2.waitKey(0)
        
        cv2.destroyAllWindows()
        h, w = img.shape[:2]
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(self.objtPoints, self.imgpoints, gray.shape[::-1], None, None)

        return str(mtx) 