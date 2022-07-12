import pyautogui as gui
import time 

import os 

IN_DIR = "/mnt/HDD-Ubuntu/documents/phd/groningen/research/experiments/images/input/mnist/mnist_50_param_03"
OUT_DIR = "/mnt/HDD-Ubuntu/documents/phd/groningen/research/experiments/images/output/mnist/data-augumentation-subset-50-param-03"

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# POSITIONS:
SPLINE_FITTING_PARAM_INPUT_POS = (1393, 166)
RUN_BUTTON_POS = (1878, 165)
INTERP_CHKBOX_POS = (1537, 165)
MORPHOTREE_BUTTON_POS = (38, 110)
ROOT_NODE_POS = (1598, 209)
SELECT_DESC_NODES_BUTTON_POS = (1488, 179)
SPLINE_MANIP_BUTTON_POS = (1802, 177)
VIS_CONTROL_POINTS_BUTTON_POS = (83, 162)
TOP_LEFT_SPLINE_MANIP_REGION = (17, 194)
BOTTOM_RIGHT_SPLINE_MANIP_REGION = (1408, 1020)
RANDOM_CHANGES_BUTTON_POS = (327, 167)
OUTPUT_DIRECTORY_INPUT_POS = (1025, 602)
START_INDEX_INPUT_POS = (903, 695)
NUMBER_OF_SAMPLES_INPUT_POS = (887, 722)
GENERATE_MULTISAMPLES_BUTTON_POS = (1079, 773)
SPLINE_REC_BUTTON_POS = (1842, 180)

# DIGIT 0
IN_FILES_0 = [
   ['1907', '3269', '4289', '6001', '6958', '7499', '8294', '9456', '9695', '10844'],
   ['10914', '10975', '13074', '13231', '16618', '16921', '18641', '18832', '19856', '19930'],
   ['20478', '20658', '22938', '23401', '26261', '27023', '28024', '28755', '33253', '34213'],
   ['37495', '39859', '39874', '40039', '40418', '41447', '43443', '47419', '47822', '48459'],
   ['49535', '50820', '53243', '55023', '55681', '56639', '56755', '56929', '57161', '58754']]
		
#DIGIT 1
IN_FILES_1 = [
   ['455', '1544', '4070', '4190', '4534', '6977', '6989', '7105', '8106', '8738'],
   ['10602', '10783', '14366', '14417', '15451', '16525', '16805', '17839', '18963', '20319'],
   ['22455', '24175', '26476', '28235', '28516', '30628', '30847', '32892', '33190', '33374'],
   ['33706', '33865', '33942', '34992', '37101', '37232', '37997', '40319', '42000', '46518'],
   ['48253', '48303', '49205', '49592', '50367', '52075', '56836', '57778', '57865', '59200']]


# DIGIT 2
IN_FILES_2 = [
   ['1264', '2105', '3390', '6386', '9054', '10945', '11095', '15699', '16235', '19545'],
   ['19721', '21615', '22198', '22442', '22606', '23764', '24035', '25329', '28052', '30309'],
   ['31221', '31757', '33160', '33250', '33435', '33743', '34444', '35347', '35489', '36142'],
   ['36170', '36942', '37646', '37743', '37942', '40152', '41398', '42686', '46543', '46619'],
   ['47557', '49907', '51379', '51614', '54553', '54805', '54848', '55952', '57694', '58267']]

# DIGIT 3
IN_FILES_3 = [
   ['255', '895', '1941', '2230', '4552', '5799', '5942', '6658', '6856', '7132'],
   ['11021', '11665', '12035', '12303', '13134', '13577', '14333', '15201', '15443', '16924'],
   ['27977', '29357', '30000', '30774', '32330', '33609', '37404', '37566', '37604', '37797'],
   ['41123', '42203', '42264', '42526', '44249', '44779', '46134', '46848', '47975', '48500'],
   ['51469', '51471', '51655', '54888', '55461', '55962', '57291', '57766', '57974', '59262']]

# DIGIT 4
IN_FILES_4 = [
   ['164', '697', '2003', '2129', '3101', '4180', '4336', '8101', '9375', '10724'],
   ['14715', '14939', '15347', '16807', '18592', '18867', '19401', '20425', '20653', '21817'],
   ['24316', '25361', '28028', '29827', '30779', '30868', '31453', '33031', '33708', '34367'],
   ['34550', '35584', '37884', '38072', '38209', '38984', '39182', '39548', '45751', '47750'],
   ['49325', '50841', '51693', '53449', '55004', '55359', '55690', '56970', '57422', '57875']]


# DIGIT 5
IN_FILES_5 = [
   ['778', '2758', '2900', '3637', '3819', '4167', '4194', '6004', '6305', '7964'],
   ['9800', '10065', '10509', '11963', '13284', '15070', '16780', '20534', '20769', '20853'],
   ['21139', '21338', '22073', '22272', '23226', '24001', '24330', '26676', '28732', '31499'],
   ['32324', '36253', '36787', '38698', '39903', '42390', '42705', '42964', '43432', '43946'],
   ['44802', '45607', '46369', '49759', '50155', '50649', '51972', '52086', '56344', '56554']]

# DIGIT 6
IN_FILES_6 = [
   ['221', '547', '1240', '3577', '4087', '4463', '4724', '4934', '4990', '6131'],
   ['9254', '9745', '13035', '14190', '14256', '16896', '17829', '18140', '21617', '22649'],
   ['22962', '23471', '23654', '24685', '29275', '29838', '29881', '30074', '30873', '31645'],
   ['31998', '34174', '38115', '40036', '41676', '43726', '44070', '45984', '46013', '46526'],
   ['46646', '48749', '50588', '50635', '50670', '51857', '52100', '54068', '55754', '59098']]

# DIGIT 7
IN_FILES_7 = [
   ['71', '3914', '7226', '9538', '11805', '11821', '12751', '12921', '13512', '16162'],
   ['20498', '23220', '24044', '24477', '24815', '25011', '25733', '26886', '27158', '27722'],
   ['27881', '27956', '28009', '29238', '29806', '30767', '31300', '34142', '34618', '36052'],
   ['36654', '37073', '38001', '39107', '40783', '42204', '44322', '44552', '45811', '46541'],
   ['47325', '47485', '48909', '49571', '50868', '54940', '56107', '58092', '58167', '59068']]

# DIGIT 8
IN_FILES_8 = [
   ['1064', '1542', '2636', '5248', '5418', '6508', '8031', '8033', '8213', '8507'],
   ['9020', '10936', '11450', '12710', '12928', '13018', '13320', '14209', '14270', '17405'],
   ['18012', '19159', '19593', '21110', '22893', '23637', '23987', '26079', '26813', '29303'],
   ['31781', '33979', '34707', '34870', '36386', '37600', '41560', '42029', '42060', '44467'],
   ['44759', '49493', '49869', '49947', '51705', '53115', '53640', '54226', '59129', '59916']]

# DIGIT 9
IN_FILES_9 = [
  ['153', '1027', '2284', '2453', '3232', '4912', '8111', '8199', '16152', '16881'],
  ['17147', '17674', '20216', '20594', '20901', '21510', '21840', '21997', '22902', '23100'],
  ['25367', '25371', '26631', '27929', '28346', '29778', '29821', '29978', '30977', '32729'],
  ['37029', '38030', '39816', '40984', '44234', '44701', '44763', '45700', '48747', '51200'],
  ['52127', '55835', '55992', '56051', '56464', '56861', '57152', '57444', '58213', '59992']]


IN_FILES = {
  "0": IN_FILES_0,
  "1": IN_FILES_1,
  "2": IN_FILES_2,
  "3": IN_FILES_3,
  "4": IN_FILES_4,
  "5": IN_FILES_5,
  "6": IN_FILES_6,
  "7": IN_FILES_7,
  "8": IN_FILES_8,
  "9": IN_FILES_9}


INITIAL_INDEX = 67200
NUMBER_OF_SAMPLES = "15"

def perform_sample_generators(in_file, start_index, digit):
  time.sleep(2)
  gui.hotkey('ctrl', 'o')  # perform open file action
  gui.hotkey('ctrl', "l")  # select location bar text
  time.sleep(2)

  # make the input file path
  in_filepath = os.path.join(IN_DIR, digit, in_file)

  gui.write(in_filepath, 0.01) # write the path to the current input image
  gui.press("enter")  # open file
  time.sleep(2)
  gui.tripleClick(SPLINE_FITTING_PARAM_INPUT_POS) # select spline fitting parameter
  time.sleep(2)
  gui.write("0,004", 0.01) # enter the 0.004 for this field
  time.sleep(1)  
  gui.click(RUN_BUTTON_POS) # click on "run" button 
  time.sleep(5)
  gui.click(INTERP_CHKBOX_POS) # select interp check box
  gui.click(MORPHOTREE_BUTTON_POS)   # click to compute max-tree
  time.sleep(5)
  gui.click(ROOT_NODE_POS) # select root node 
  time.sleep(1)
  gui.click(SELECT_DESC_NODES_BUTTON_POS) # click on select descendant nodes button
  time.sleep(1)
  with gui.hold("shift"):
    gui.click(ROOT_NODE_POS) # deselect root node

  time.sleep(1) 
  gui.click(SPLINE_MANIP_BUTTON_POS) # click on spline manipulation button
  time.sleep(1)
  gui.click(VIS_CONTROL_POINTS_BUTTON_POS) # click on visualise control points button
  time.sleep(1)

  # draw a selection rectagle that covers all control points (entire canvas) 
  gui.moveTo(TOP_LEFT_SPLINE_MANIP_REGION) 
  gui.dragTo(BOTTOM_RIGHT_SPLINE_MANIP_REGION)

  time.sleep(1)
  gui.click(RANDOM_CHANGES_BUTTON_POS) # click on the random changes button
  time.sleep(2)
  gui.tripleClick(OUTPUT_DIRECTORY_INPUT_POS) # select output directory input
  time.sleep(1)
  out_dir = os.path.join(OUT_DIR, digit) # create ouput path
  gui.write(out_dir, 0.01) # write output path to the output directory input
  gui.doubleClick(START_INDEX_INPUT_POS) # select start index input
  time.sleep(2)
  gui.write(start_index, 0.01) # write start index to its input
  gui.doubleClick(NUMBER_OF_SAMPLES_INPUT_POS) # select number of samples input 
  time.sleep(2)
  gui.write(NUMBER_OF_SAMPLES) # write number of samples to its input
  time.sleep(1)
  gui.click(GENERATE_MULTISAMPLES_BUTTON_POS) # click on "generate multi-samples" button.
  time.sleep(15)
  gui.click(SPLINE_REC_BUTTON_POS) # click on spline reconstruction button to go back at the intial window
  time.sleep(1)
  gui.click(MORPHOTREE_BUTTON_POS) # click on the morphotree button to remove it 
  time.sleep(1)
  gui.click(INTERP_CHKBOX_POS) # unselect "interp" check box

index = INITIAL_INDEX
for digit in DIGITS:
  for batch in IN_FILES[digit]:
    time.sleep(5)
    gui.write("./bin/interactive-dmd\n") # open application
    time.sleep(5)
    gui.hotkey("alt", "f10") # maximise window
   
    for in_filename in batch:
       print(f"{in_filename} - {index}")
       perform_sample_generators(in_filename + ".pgm", str(index), digit)
       index += int(NUMBER_OF_SAMPLES)

    gui.hotkey("alt", "f4")
    time.sleep(20)