import dlib

dat = "custom_predictor.dat"
xml = "labels_ibug_300W_test_custom.xml"

print("[INFO] evaluating shape predictor...")
error = dlib.test_shape_predictor(xml, dat)
print("[INFO] error: {}".format(error))
