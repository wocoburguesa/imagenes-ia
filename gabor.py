# encoding: utf-8
# gabor.py
# 2012-3-8
# Eiichiro Momma
__author__ = 'momma'
import numpy as np
import cv2 as cv
def mkKernel(ks, sig, th , lm, ps):
    if not ks%2:
        exit(1)
    hks = ks/2
    theta = th * np.pi/180.
    psi = ps * np.pi/180.
    xs=np.linspace(-1.,1.,ks)
    ys=np.linspace(-1.,1.,ks)
    lmbd = np.float(lm)
    x,y = np.meshgrid(xs,ys)
    sigma = np.float(sig)/ks
    x_theta = x*np.cos(theta)+y*np.sin(theta)
    y_theta = -x*np.sin(theta)+y*np.cos(theta)
    return np.array(np.exp(-0.5*(x_theta**2+y_theta**2)/sigma**2)*np.cos(2.*np.pi*x_theta/lmbd + psi),dtype=np.float32)

src_f = 0

kernel_size = 20
pos_sigma = 5
pos_lm = 50
pos_th = 0
pos_psi = 90

def Process():
    sig = pos_sigma
    lm = 0.5+pos_lm/100.
    th = pos_th
    ps = pos_psi
    kernel = mkKernel(kernel_size, sig, th, lm, ps )
    kernelimg = kernel/2.+0.5
    global src_f
    dest = cv.filter2D(src_f, cv.CV_32F,kernel)
    cv.imshow('Process window', dest)
    cv.imshow('Kernel', cv.resize(kernelimg, (kernel_size*20,kernel_size*20)))
    cv.imshow('Mag', np.power(dest,2))

def cb_sigma(pos):
    global pos_sigma
    if pos > 0:
        pos_sigma = pos
    else:
        pos_sigma = 1
    Process()

def cb_lm(pos):
    global pos_lm
    pos_lm = pos
    Process()

def cb_th(pos):
    global pos_th
    pos_th = pos
    Process()

def cb_psi(pos):
    global pos_psi
    pos_psi = pos
    Process()

if __name__ == '__main__':
    image = cv.imread("irma100/HEA_2971.jpg",1);
    cv.imshow('Src',image)
    src = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        #global src_f
    src_f = np.array(src, dtype=np.float32)
    src_f /= 255.
    if not kernel_size%2:
        kernel_size += 1

    cv.namedWindow('Process window',1)
    cv.createTrackbar('Sigma','Process window',pos_sigma,kernel_size,cb_sigma)
    cv.createTrackbar('Lambda', 'Process window', pos_lm, 100, cb_lm)
    cv.createTrackbar('Phase', 'Process window', pos_th, 180, cb_th)
    cv.createTrackbar('Psi', 'Process window', pos_psi, 360, cb_psi)
    Process()
    cv.waitKey(0)
    cv.destroyAllWindows()
