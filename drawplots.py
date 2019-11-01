import os, subprocess, sys, glob, shutil, csv, getopt
import numpy as np
import matplotlib.pyplot as plt

NestList_size_compaction = [['ex3_e7_590_e8_550.c', '34', '34'], ['ex3_e8_381_e7_224.c', '34', '34'], ['cd_e7_621_e8_714.c', '64', '65'], ['cruise_controller_09.c', '36', '41'], ['rtp_1.c', '64', '64'], ['tramway_e7_1834.c', '117', '133'], ['hysteresis_3.c', '34', '34'], ['SYNAPSE_4_e8_420_e8_1525.c', '51', '59'], ['PRODUCER_CONSUMER_2.c', '54', '90'], ['car_all_e2_108.c', '47', '55'], ['cd.c', '117', '129'], ['cruise_controller_23.c', '34', '34'], ['car_3_e2_695.c', '44', '51'], ['fast_1_e8_747_e8_1041.c', '34', '34'], ['fast_2_e7_2526_e8_1145.c', '49', '59'], ['hysteresis_all.c', '37', '37'], ['car_2.c', '44', '51'], ['fast_2_e8_460_e8_1920.c', '49', '49'], ['tramway_e7_1834_e7_2363.c', '117', '133'], ['fast_1_e8_747.c', '34', '34'], ['speed_e8_649_e7_709.c', '37', '37'], ['car_4_e3_57_e4_1047.c', '44', '51'], ['car_3_e8_33.c', '44', '51'], ['car_all_e8_856.c', '47', '55'], ['cruise_controller_17.c', '37', '37'], ['car_all_e2_142_e8_194.c', '47', '55'], ['hysteresis_1.c', '37', '37'], ['car_3.c', '44', '51'], ['cruise_controller_06.c', '34', '34'], ['car_3_e8_33_e7_220.c', '44', '51'], ['cruise_controller_07.c', '34', '34'], ['fast_2_e8_460.c', '49', '49'], ['car_4_e7_592.c', '44', '51'], ['car_3_e8_33_e2_1010.c', '44', '51'], ['speed_e7_207.c', '37', '37'], ['cruise_controller_20.c', '34', '34'], ['cruise_controller_16.c', '37', '37'], ['hysteresis_2.c', '34', '34'], ['speed_e7_207_e7_538.c', '37', '37'], ['ex3_e7_590_e7_590.c', '34', '34'], ['car_all_e3_1068_e6_790.c', '47', '55'], ['cruise_controller_11.c', '37', '37'], ['ex3_e7_590.c', '34', '34'], ['speed_e7_207_e8_507.c', '37', '37'], ['cruise_controller_15.c', '37', '37'], ['car_all_e3_1068_e4_275.c', '47', '55'], ['car_1.c', '44', '51'], ['speed_e8_136.c', '37', '37'], ['SYNAPSE_2_e8_1118_e7_1043.c', '54', '63'], ['car_4_e8_118.c', '44', '51'], ['fast_1_e7_2044_e8_1396.c', '34', '34'], ['car_3_e7_626.c', '44', '51'], ['car_4_e3_57_e6_784.c', '44', '51'], ['ex3_e8_120.c', '34', '34'], ['HacmsTiming_M1.c', '44', '44'], ['SmaccmPhase2_V3_nav_t.c', '34', '34'], ['Speed_Control.c', '50', '50'], ['SmaccmPhase2_V3_mavlink_t.c', '37', '37'], ['Integer_Toy_Extended_A.c', '36', '36'], ['Rise.c', '48', '48'], ['Throttle.c', '36', '36'], ['HacmsTiming_M3.c', '51', '51'], ['Integer_Toy_Extended_C.c', '38', '38'], ['OutputBus.c', '184', '184'], ['Real_Toy_top_level.c', '34', '34'], ['Integer_Toy_Extended_top_level.c', '34', '34'], ['Mode_Control_TheArchitects.c', '98', '98'], ['System_Status.c', '60', '65'], ['Mode_Control_eTeam.c', '104', '104'], ['Autopilot_System.c', '63', '69'], ['Real_Toy_C.c', '38', '38'], ['Mode_Control_4_Horsemen.c', '98', '98'], ['SmaccmPhase2_V3_transmit_t.c', '34', '34'], ['Pilot_Flying.c', '95', '101'], ['SmaccmPhase2_V3_can_px4_t.c', '49', '49'], ['SmaccmPhase2_V3_encrypt_t.c', '34', '34'], ['consistency_test_C1.c', '37', '37'], ['Mode_Control_FiveGuys.c', '98', '98'], ['Mode_Control_sfurtney.c', '80', '80'], ['Mode_Control_phil.c', '98', '98'], ['Sub_State_Machine.c', '34', '34'], ['QuasiTest_Vehicle.c', '179', '315'], ['FCS.c', '1042', '1042'], ['Integer_Toy_Extended_B.c', '36', '36'], ['SmaccmPhase2_V3_decrypt_t.c', '37', '37'], ['SmaccmPhase2_V3_ppm_t.c', '45', '45'], ['GPCA_SW.c', '134', '161'], ['SmaccmPhase2_V3_can_a15_t.c', '46', '46'], ['Mode_Control_Global_Team.c', '98', '98'], ['Microwave_Display_Control.c', '31', '31'], ['HacmsTiming_top_level.c', '48', '49'], ['SmaccmPhase2_V3_motmix_t.c', '43', '43'], ['Steering.c', '54', '65'], ['CLAW.c', '346', '346'], ['Microwave_Mode_Control.c', '58', '58'], ['Infusion_Manager.c', '121', '193'], ['Fall.c', '48', '48'], ['HacmsTiming_M2.c', '44', '44'], ['Real_Toy_B.c', '36', '36'], ['Real_Toy_A.c', '36', '36'], ['Integer_Toy_Extended_above_top.c', '34', '34'], ['QuasiTest_Squadron.c', '49', '49'], ['Config.c', '52', '52'], ['State_Machine.c', '31', '31'], ['Top_Level_Mode.c', '47', '49'], ['SmaccmPhase2_V3_receive_t.c', '37', '37'], ['BSCU_COM.c', '512', '2349'], ['Alarm.c', '96', '176'], ['newexample.c', '62', '70'], ['nfmexample_1.c', '43', '43'], ['nfmexample_2.c', '55', '68'], ['example.c', '62', '84'], ['nfmexample.c', '43', '43'], ['mwwex.c', '39', '39'], ['cinderella_1.c', '109', '149'], ['Dual_FGS_aadl_FCS.c', '91', '91'], ['SmaccmPhase2_V3_Flight_Software.c', '143', '164'], ['SmaccmPhase2_V3_Mission_Software.c', '132', '155'], ['cinderella.c', '112', '139'], ['cinderella_2.c', '204', '279'], ['cinderella_4.c', '204', '329'], ['cinderella_3.c', '119', '149']]

NestList_overhead = [['ex3_e7_590_e8_550.lus', '0.1', '0.302', '0.202'], ['ex3_e8_381_e7_224.lus', '0.1', '0.303', '0.202'], ['cd_e7_621_e8_714.lus', '0.201', '0.718', '0.302'], ['cruise_controller_09.lus', '0.101', '0.302', '0.202'], ['rtp_1.lus', '0.202', '0.505', '0.303'], ['tramway_e7_1834.lus', '0.909', '1.515', '0.707'], ['hysteresis_3.lus', '0.101', '0.302', '0.202'], ['SYNAPSE_4_e8_420_e8_1525.lus', '0.101', '0.303', '0.201'], ['PRODUCER_CONSUMER_2.lus', '0.101', '0.606', '0.302'], ['car_all_e2_108.lus', '0.101', '0.406', '0.301'], ['cd.lus', '0.405', '2.007', '1.002'], ['cruise_controller_23.lus', '0.101', '0.303', '0.202'], ['car_3_e2_695.lus', '0.101', '0.304', '0.201'], ['fast_1_e8_747_e8_1041.lus', '0.101', '0.301', '0.201'], ['fast_2_e7_2526_e8_1145.lus', '0.101', '0.503', '0.201'], ['hysteresis_all.lus', '0.101', '0.302', '0.202'], ['car_2.lus', '0.406', '0.302', '0.201'], ['fast_2_e8_460_e8_1920.lus', '0.1', '0.504', '0.403'], ['tramway_e7_1834_e7_2363.lus', '1.11', '1.713', '0.807'], ['fast_1_e8_747.lus', '0.202', '0.301', '0.202'], ['speed_e8_649_e7_709.lus', '0.102', '0.302', '0.201'], ['car_4_e3_57_e4_1047.lus', '0.1', '0.303', '0.202'], ['car_3_e8_33.lus', '0.101', '0.303', '0.201'], ['car_all_e8_856.lus', '0.101', '0.711', '0.303'], ['cruise_controller_17.lus', '0.202', '0.403', '0.202'], ['car_all_e2_142_e8_194.lus', '0.101', '0.505', '0.302'], ['hysteresis_1.lus', '0.1', '0.302', '0.305'], ['car_3.lus', '0.101', '0.303', '0.201'], ['cruise_controller_06.lus', '0.101', '0.404', '0.202'], ['car_3_e8_33_e7_220.lus', '0.101', '0.301', '0.201'], ['cruise_controller_07.lus', '0.101', '0.301', '0.201'], ['fast_2_e8_460.lus', '0.303', '0.401', '0.302'], ['car_4_e7_592.lus', '0.1', '0.3', '0.202'], ['car_3_e8_33_e2_1010.lus', '0.102', '0.402', '0.203'], ['speed_e7_207.lus', '0.107', '0.303', '0.201'], ['cruise_controller_20.lus', '0.101', '0.302', '0.201'], ['cruise_controller_16.lus', '0.101', '0.303', '0.202'], ['hysteresis_2.lus', '0.1', '0.303', '0.201'], ['speed_e7_207_e7_538.lus', '0.101', '0.202', '0.101'], ['ex3_e7_590_e7_590.lus', '0.1', '0.303', '0.201'], ['car_all_e3_1068_e6_790.lus', '0.203', '0.705', '0.302'], ['cruise_controller_11.lus', '0.101', '0.303', '0.203'], ['ex3_e7_590.lus', '0.1', '0.303', '0.202'], ['speed_e7_207_e8_507.lus', '0.101', '0.305', '0.203'], ['cruise_controller_15.lus', '0.101', '0.404', '0.202'], ['car_all_e3_1068_e4_275.lus', '0.101', '0.504', '0.303'], ['car_1.lus', '0.204', '0.404', '0.201'], ['speed_e8_136.lus', '0.101', '0.302', '0.204'], ['SYNAPSE_2_e8_1118_e7_1043.lus', '0.203', '0.708', '0.303'], ['car_4_e8_118.lus', '0.202', '0.403', '0.202'], ['fast_1_e7_2044_e8_1396.lus', '0.101', '0.404', '0.201'], ['car_3_e7_626.lus', '0.202', '0.302', '0.201'], ['car_4_e3_57_e6_784.lus', '0.201', '0.303', '0.202'], ['ex3_e8_120.lus', '0.101', '0.305', '0.202'], ['HacmsTiming_M1.lus', '0.101', '0.303', '0.202'], ['SmaccmPhase2_V3_nav_t.lus', '0.102', '0.301', '0.1'], ['Speed_Control.lus', '0.201', '0.302', '0.202'], ['SmaccmPhase2_V3_mavlink_t.lus', '0.101', '0.303', '0.2'], ['Integer_Toy_Extended_A.lus', '0.101', '0.202', '0.322'], ['Rise.lus', '0.101', '1.008', '0.201'], ['Throttle.lus', '0.1', '0.303', '0.201'], ['HacmsTiming_M3.lus', '0.101', '0.404', '0.202'], ['Integer_Toy_Extended_C.lus', '0.101', '0.304', '0.261'], ['OutputBus.lus', '0.403', '0.806', '0.611'], ['Real_Toy_top_level.lus', '0.2', '0.202', '0.202'], ['Integer_Toy_Extended_top_level.lus', '0.101', '0.201', '0.2'], ['Mode_Control_TheArchitects.lus', '0.201', '0.906', '0.504'], ['System_Status.lus', '0.202', '0.403', '0.202'], ['Mode_Control_eTeam.lus', '0.307', '0.808', '0.504'], ['Autopilot_System.lus', '0.101', '1.62', '0.818'], ['Real_Toy_C.lus', '0.101', '0.302', '0.202'], ['Mode_Control_4_Horsemen.lus', '0.203', '0.809', '0.404'], ['SmaccmPhase2_V3_transmit_t.lus', '0.101', '0.306', '0.201'], ['Pilot_Flying.lus', '0.505', '1.615', '1.21'], ['SmaccmPhase2_V3_can_px4_t.lus', '0.101', '0.405', '0.202'], ['SmaccmPhase2_V3_encrypt_t.lus', '0.101', '0.202', '0.101'], ['consistency_test_C1.lus', '0.102', '0.303', '0.202'], ['Mode_Control_FiveGuys.lus', '0.202', '0.809', '0.403'], ['Mode_Control_sfurtney.lus', '0.202', '0.807', '0.403'], ['Mode_Control_phil.lus', '0.203', '0.833', '0.504'], ['Sub_State_Machine.lus', '0.101', '0.303', '0.202'], ['QuasiTest_Vehicle.lus', '0.51', '9.803', '5.867'], ['FCS.lus', '1.821', '282.361', '133.741'], ['Integer_Toy_Extended_B.lus', '0.101', '0.301', '0.202'], ['SmaccmPhase2_V3_decrypt_t.lus', '0.101', '0.302', '0.201'], ['SmaccmPhase2_V3_ppm_t.lus', '0.102', '0.303', '0.201'], ['GPCA_SW.lus', '0.303', '1.508', '0.806'], ['SmaccmPhase2_V3_can_a15_t.lus', '0.101', '0.302', '0.205'], ['Mode_Control_Global_Team.lus', '0.203', '0.807', '0.403'], ['Microwave_Display_Control.lus', '0.103', '0.303', '0.2'], ['HacmsTiming_top_level.lus', '0.1', '0.405', '0.201'], ['SmaccmPhase2_V3_motmix_t.lus', '0.101', '0.303', '0.202'], ['Steering.lus', '0.101', '0.303', '0.202'], ['CLAW.lus', '0.202', '4.332', '2.217'], ['Microwave_Mode_Control.lus', '0.201', '0.404', '0.303'], ['Infusion_Manager.lus', '0.303', '2.522', '1.311'], ['Fall.lus', '0.101', '0.407', '0.201'], ['HacmsTiming_M2.lus', '0.101', '0.303', '0.202'], ['Real_Toy_B.lus', '0.101', '0.302', '0.201'], ['Real_Toy_A.lus', '0.103', '0.201', '0.203'], ['Integer_Toy_Extended_above_top.lus', '0.102', '0.202', '0.1'], ['QuasiTest_Squadron.lus', '0.101', '0.402', '0.202'], ['Config.lus', '0.101', '0.303', '0.203'], ['State_Machine.lus', '0.101', '0.303', '0.101'], ['Top_Level_Mode.lus', '0.101', '0.303', '0.202'], ['SmaccmPhase2_V3_receive_t.lus', '0.1', '0.303', '0.202'], ['BSCU_COM.lus', '1.412', '65.293', '31.881'], ['Alarm.lus', '0.202', '1.817', '0.807'], ['newexample.lus', '0.203', '3.23', '1.814'], ['nfmexample_1.lus', '0.204', '0.504', '0.303'], ['nfmexample_2.lus', '0.203', '0.907', '0.402'], ['example.lus', '0.201', '2.626', '2.015'], ['nfmexample.lus', '0.101', '0.304', '0.202']]

NestList_size = [['ex3_e7_590_e8_550.c', '34', '34'], ['ex3_e8_381_e7_224.c', '34', '34'], ['cd_e7_621_e8_714.c', '65', '65'], ['cruise_controller_09.c', '41', '41'], ['rtp_1.c', '64', '64'], ['tramway_e7_1834.c', '133', '133'], ['hysteresis_3.c', '34', '34'], ['SYNAPSE_4_e8_420_e8_1525.c', '59', '59'], ['PRODUCER_CONSUMER_2.c', '90', '90'], ['car_all_e2_108.c', '55', '55'], ['cd.c', '129', '129'], ['cruise_controller_23.c', '34', '34'], ['car_3_e2_695.c', '51', '51'], ['fast_1_e8_747_e8_1041.c', '34', '34'], ['fast_2_e7_2526_e8_1145.c', '59', '59'], ['hysteresis_all.c', '37', '37'], ['car_2.c', '51', '51'], ['fast_2_e8_460_e8_1920.c', '49', '49'], ['tramway_e7_1834_e7_2363.c', '133', '133'], ['fast_1_e8_747.c', '34', '34'], ['speed_e8_649_e7_709.c', '37', '37'], ['car_4_e3_57_e4_1047.c', '51', '51'], ['car_3_e8_33.c', '51', '51'], ['car_all_e8_856.c', '55', '55'], ['cruise_controller_17.c', '37', '37'], ['car_all_e2_142_e8_194.c', '55', '55'], ['hysteresis_1.c', '37', '37'], ['car_3.c', '51', '51'], ['cruise_controller_06.c', '34', '34'], ['car_3_e8_33_e7_220.c', '51', '51'], ['cruise_controller_07.c', '34', '34'], ['fast_2_e8_460.c', '49', '49'], ['car_4_e7_592.c', '51', '51'], ['car_3_e8_33_e2_1010.c', '51', '51'], ['speed_e7_207.c', '37', '37'], ['cruise_controller_20.c', '34', '34'], ['cruise_controller_16.c', '37', '37'], ['hysteresis_2.c', '34', '34'], ['speed_e7_207_e7_538.c', '37', '37'], ['ex3_e7_590_e7_590.c', '34', '34'], ['car_all_e3_1068_e6_790.c', '55', '55'], ['cruise_controller_11.c', '37', '37'], ['ex3_e7_590.c', '34', '34'], ['speed_e7_207_e8_507.c', '37', '37'], ['cruise_controller_15.c', '37', '37'], ['car_all_e3_1068_e4_275.c', '55', '55'], ['car_1.c', '51', '51'], ['speed_e8_136.c', '37', '37'], ['SYNAPSE_2_e8_1118_e7_1043.c', '63', '63'], ['car_4_e8_118.c', '51', '51'], ['fast_1_e7_2044_e8_1396.c', '34', '34'], ['car_3_e7_626.c', '51', '51'], ['car_4_e3_57_e6_784.c', '51', '51'], ['ex3_e8_120.c', '34', '34'], ['HacmsTiming_M1.c', '44', '44'], ['SmaccmPhase2_V3_nav_t.c', '34', '34'], ['Speed_Control.c', '50', '50'], ['SmaccmPhase2_V3_mavlink_t.c', '37', '37'], ['Integer_Toy_Extended_A.c', '36', '36'], ['Rise.c', '48', '48'], ['Throttle.c', '36', '36'], ['HacmsTiming_M3.c', '51', '51'], ['Integer_Toy_Extended_C.c', '38', '38'], ['OutputBus.c', '184', '184'], ['Real_Toy_top_level.c', '34', '34'], ['Integer_Toy_Extended_top_level.c', '34', '34'], ['Mode_Control_TheArchitects.c', '98', '98'], ['System_Status.c', '65', '65'], ['Mode_Control_eTeam.c', '104', '104'], ['Autopilot_System.c', '69', '69'], ['Real_Toy_C.c', '38', '38'], ['Mode_Control_4_Horsemen.c', '98', '98'], ['SmaccmPhase2_V3_transmit_t.c', '34', '34'], ['Pilot_Flying.c', '174', '101'], ['SmaccmPhase2_V3_can_px4_t.c', '49', '49'], ['SmaccmPhase2_V3_encrypt_t.c', '34', '34'], ['consistency_test_C1.c', '37', '37'], ['Mode_Control_FiveGuys.c', '98', '98'], ['Mode_Control_sfurtney.c', '80', '80'], ['Mode_Control_phil.c', '98', '98'], ['Sub_State_Machine.c', '34', '34'], ['QuasiTest_Vehicle.c', '632', '315'], ['FCS.c', '1042', '1042'], ['Integer_Toy_Extended_B.c', '36', '36'], ['SmaccmPhase2_V3_decrypt_t.c', '37', '37'], ['SmaccmPhase2_V3_ppm_t.c', '45', '45'], ['GPCA_SW.c', '161', '161'], ['SmaccmPhase2_V3_can_a15_t.c', '46', '46'], ['Mode_Control_Global_Team.c', '98', '98'], ['Microwave_Display_Control.c', '31', '31'], ['HacmsTiming_top_level.c', '49', '49'], ['SmaccmPhase2_V3_motmix_t.c', '43', '43'], ['Steering.c', '65', '65'], ['CLAW.c', '346', '346'], ['Microwave_Mode_Control.c', '58', '58'], ['Infusion_Manager.c', '193', '193'], ['Fall.c', '48', '48'], ['HacmsTiming_M2.c', '44', '44'], ['Real_Toy_B.c', '36', '36'], ['Real_Toy_A.c', '36', '36'], ['Integer_Toy_Extended_above_top.c', '34', '34'], ['QuasiTest_Squadron.c', '49', '49'], ['Config.c', '52', '52'], ['State_Machine.c', '31', '31'], ['Top_Level_Mode.c', '49', '49'], ['SmaccmPhase2_V3_receive_t.c', '37', '37'], ['BSCU_COM.c', '2349', '2349'], ['Alarm.c', '176', '176'], ['newexample.c', '126', '70'], ['nfmexample_1.c', '56', '43'], ['nfmexample_2.c', '134', '68'], ['example.c', '98', '84'], ['nfmexample.c', '43', '43']]

NestList_performance = [['ex3_e7_590_e8_550', '13.295000', '13.572000'], ['ex3_e8_381_e7_224', '13.371000', '14.445000'], ['cd_e7_621_e8_714', '38.158000', '38.376000'], ['cruise_controller_09', '24.630000', '24.514000'], ['rtp_1', '284.325000', '285.246000'], ['tramway_e7_1834', '198.179000', '199.442000'], ['hysteresis_3', '13.986000', '13.322000'], ['SYNAPSE_4_e8_420_e8_1525', '101.008000', '100.644000'], ['PRODUCER_CONSUMER_2', '107.854000', '107.043000'], ['car_all_e2_108', '64.300000', '63.459000'], ['cd', '51.147000', '51.983000'], ['cruise_controller_23', '10.419000', '10.514000'], ['car_3_e2_695', '61.120000', '62.207000'], ['fast_1_e8_747_e8_1041', '13.619000', '13.311000'], ['fast_2_e7_2526_e8_1145', '21.689000', '22.231000'], ['hysteresis_all', '11.462000', '11.791000'], ['car_2', '61.153000', '61.169000'], ['fast_2_e8_460_e8_1920', '21.062000', '20.823000'], ['tramway_e7_1834_e7_2363', '194.669000', '197.300000'], ['fast_1_e8_747', '13.690000', '13.181000'], ['speed_e8_649_e7_709', '12.397000', '11.997000'], ['car_4_e3_57_e4_1047', '60.076000', '60.523000'], ['car_3_e8_33', '60.428000', '61.122000'], ['car_all_e8_856', '62.960000', '63.171000'], ['cruise_controller_17', '12.487000', '12.314000'], ['car_all_e2_142_e8_194', '62.371000', '63.693000'], ['hysteresis_1', '11.626000', '11.937000'], ['car_3', '61.310000', '61.298000'], ['cruise_controller_06', '9.873000', '10.198000'], ['car_3_e8_33_e7_220', '60.634000', '60.540000'], ['cruise_controller_07', '10.485000', '9.752000'], ['fast_2_e8_460', '21.749000', '21.514000'], ['car_4_e7_592', '60.683000', '61.033000'], ['car_3_e8_33_e2_1010', '61.460000', '60.839000'], ['speed_e7_207', '11.986000', '11.463000'], ['cruise_controller_20', '10.560000', '10.506000'], ['cruise_controller_16', '12.340000', '12.017000'], ['hysteresis_2', '13.139000', '13.160000'], ['speed_e7_207_e7_538', '11.961000', '11.639000'], ['ex3_e7_590_e7_590', '14.032000', '13.719000'], ['car_all_e3_1068_e6_790', '63.803000', '65.494000'], ['cruise_controller_11', '11.906000', '12.109000'], ['ex3_e7_590', '21.574000', '13.410000'], ['speed_e7_207_e8_507', '11.382000', '11.566000'], ['cruise_controller_15', '12.041000', '12.052000'], ['car_all_e3_1068_e4_275', '62.207000', '65.094000'], ['car_1', '61.245000', '61.660000'], ['speed_e8_136', '11.766000', '11.457000'], ['SYNAPSE_2_e8_1118_e7_1043', '110.537000', '113.227000'], ['car_4_e8_118', '62.044000', '61.155000'], ['fast_1_e7_2044_e8_1396', '13.201000', '13.408000'], ['car_3_e7_626', '59.876000', '60.570000'], ['car_4_e3_57_e6_784', '60.671000', '61.377000'], ['ex3_e8_120', '13.220000', '13.323000'], ['HacmsTiming_M1', '56.780000', '56.373000'], ['SmaccmPhase2_V3_nav_t', '13.432000', '13.298000'], ['Speed_Control', '61.313000', '59.388000'], ['SmaccmPhase2_V3_mavlink_t', '11.989000', '11.632000'], ['Integer_Toy_Extended_A', '26.947000', '27.005000'], ['Rise', '44.707000', '45.128000'], ['Throttle', '27.353000', '27.084000'], ['HacmsTiming_M3', '100.518000', '103.408000'], ['Integer_Toy_Extended_C', '41.154000', '40.993000'], ['OutputBus', '576.315000', '579.807000'], ['Real_Toy_top_level', '10.500000', '10.251000'], ['Integer_Toy_Extended_top_level', '10.718000', '10.692000'], ['Mode_Control_TheArchitects', '93.302000', '96.339000'], ['System_Status', '77.724000', '78.878000'], ['Mode_Control_eTeam', '92.740000', '92.745000'], ['Autopilot_System', '112.433000', '117.343000'], ['Real_Toy_C', '42.834000', '43.135000'], ['Mode_Control_4_Horsemen', '93.000000', '91.802000'], ['SmaccmPhase2_V3_transmit_t', '13.399000', '13.271000'], ['Pilot_Flying', '86.114000', '71.145000'], ['SmaccmPhase2_V3_can_px4_t', '21.125000', '21.704000'], ['SmaccmPhase2_V3_encrypt_t', '13.349000', '13.645000'], ['consistency_test_C1', '13.136000', '11.078000'], ['Mode_Control_FiveGuys', '89.000000', '90.094000'], ['Mode_Control_sfurtney', '90.071000', '82.442000'], ['Mode_Control_phil', '91.406000', '92.395000'], ['Sub_State_Machine', '13.460000', '11.551000'], ['QuasiTest_Vehicle', '160.628000', '171.307000'], ['FCS', '979.562000', '978.381000'], ['Integer_Toy_Extended_B', '25.991000', '24.840000'], ['SmaccmPhase2_V3_decrypt_t', '11.478000', '11.232000'], ['SmaccmPhase2_V3_ppm_t', '31.070000', '37.392000'], ['GPCA_SW', '142.095000', '142.516000'], ['SmaccmPhase2_V3_can_a15_t', '18.382000', '19.231000'], ['Mode_Control_Global_Team', '90.045000', '89.081000'], ['Microwave_Display_Control', '12.692000', '12.945000'], ['HacmsTiming_top_level', '34.763000', '34.133000'], ['SmaccmPhase2_V3_motmix_t', '15.026000', '15.086000'], ['Steering', '57.481000', '57.813000'], ['CLAW', '265.706000', '262.732000'], ['Microwave_Mode_Control', '26.045000', '26.893000'], ['Infusion_Manager', '156.443000', '156.111000'], ['Fall', '43.960000', '44.206000'], ['HacmsTiming_M2', '56.218000', '55.741000'], ['Real_Toy_B', '26.359000', '26.088000'], ['Real_Toy_A', '26.408000', '26.382000'], ['Integer_Toy_Extended_above_top', '11.238000', '10.422000'], ['QuasiTest_Squadron', '20.775000', '20.541000'], ['Config', '22.810000', '22.763000'], ['State_Machine', '12.778000', '12.012000'], ['Top_Level_Mode', '40.356000', '39.544000'], ['SmaccmPhase2_V3_receive_t', '11.399000', '11.644000'], ['BSCU_COM', '776.103000', '768.434000'], ['Alarm', '127.145000', '127.171000'], ['newexample', '52.876000', '52.977000'], ['nfmexample_1', '56.104000', '52.302000'], ['nfmexample_2', '76.987000', '61.591000'], ['example', '51.789000', '57.245000'], ['nfmexample', '50.785000', '50.488000']]


def getMax(nList):
    sList1 = sorted(nList, key=lambda x: float(x[1]))
    sList2 = sorted(nList, key=lambda x: float(x[2]))
    if (sList1[-1][1] >= sList2[-1][2]):
        return sList1[-1][1]
    else:
        return sList2[-1][2]

def drawPerformance():
    font = {'family' : 'normal','weight' : 'bold','size' : 20}
    plt.rc('font', **font)

    pl1 = np.array([float(j[1]) for j in NestList_performance])
    pl2 = np.array([float(j[2]) for j in NestList_performance])

    fig = plt.figure()

    plt.scatter(pl1,pl2,c="r", s = 100,edgecolor= "")
    plt.axis([0,(float(getMax(NestList_performance))+20),0,(float(getMax(NestList_performance))+20)])
    plt.plot([0,(float(getMax(NestList_performance))+20)],[0,(float(getMax(NestList_performance))+20)])

    plt.xlabel("JSYN")
    plt.ylabel("JSYN-VG")
    plt.title("Performance(milliseconds)")
    plt.legend(loc = 'upper left')
    fig.savefig("performance.pdf")




def drawOverhead():
    font = {'family' : 'normal','weight' : 'bold', 'size' : 20}
    plt.rc('font', **font)

    pl1 = np.array([float(j[1]) for j in sorted(NestList_overhead,key=lambda  x: float(x[3]))])
    pl2 = np.array([float(j[2]) for j in sorted(NestList_overhead,key=lambda  x: float(x[3]))])
    pl3 = np.array([float(j[3]) for j in sorted(NestList_overhead,key=lambda  x: float(x[3]))])

    fig = plt.figure()

    plt.scatter(pl2,pl3,c="r", s = 100,edgecolor= "")

    plt.yscale('log')
    plt.xscale('log')
    plt.axis([0,(float(getMax(NestList_overhead))+20),0,(float(getMax(NestList_overhead))+20)])
    plt.plot([0,(float(getMax(NestList_overhead))+20)],[0,(float(getMax(NestList_overhead))+20)])

    plt.xlabel("JSYN")
    plt.ylabel("JSYN-VG")
    plt.title("Performance(seconds)")
    plt.legend(loc = 'upper left')
    fig.savefig("overhead.pdf")

    #plt.yscale('log')
    #plt.ylim(pow(10,-1), pow(10,2.8))

    #synthesis = plt.plot(pl2,'-r^', label = 'JSYN', markersize = 10)
    #fixpoint = plt.plot(pl3,'-bo', label = 'JSYN-VG',  markersize = 10)

    #plt.xlabel("Model")
    #plt.ylabel("Performance(seconds)")
    #plt.legend(loc = 'upper left')
    #fig.savefig("overhead.pdf")

def drawSize():
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 20}
    plt.rc('font', **font)

    pl1 = np.array([j[1] for j in sorted(NestList_size, key=lambda x: float(x[2]))])
    pl2 = np.array([j[2] for j in sorted(NestList_size, key=lambda x: float(x[2]))])
# Plot the results


    fig = plt.figure()

    
    plt.scatter(pl1,pl2,c="r", s = 100,edgecolor= "")
    plt.yscale('log')
    plt.xscale('log')

    plt.axis([0,(float(getMax(NestList_size))+200),0,(float(getMax(NestList_size))+200)])
    plt.plot([0,(float(getMax(NestList_size))+200)],[0,(float(getMax(NestList_size))+200)])

    plt.xlabel("JSYN")
    plt.ylabel("JSYN-VG")
    plt.title("Lines of Code")
    plt.legend(loc = 'upper left')
    fig.savefig("loc.pdf")

    
    #plt.yscale('log')
    #plt.ylim(pow(10,1), pow(10,3.5))
    #synthesized = plt.plot(pl1,'-r^', label = 'JSYN', markersize = 10)
    #fixpoint = plt.plot(pl2,'-bo', label = 'JSYN-VG', markersize = 7)

    #plt.xlabel("Model")
    #plt.ylabel("Lines of Code")
    #plt.legend(loc = 'upper left')
    #fig.savefig("loc.pdf")

def drawFixpointReducedSize():
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 20}
    plt.rc('font', **font)


    pl1 = np.array([j[1] for j in sorted(NestList_size_compaction, key=lambda x: float(x[2]))])
    pl2 = np.array([j[2] for j in sorted(NestList_size_compaction, key=lambda x: float(x[2]))])
# Plot the results


    fig = plt.figure()


    plt.scatter(pl1,pl2,c="r", s = 100,edgecolor= "")
    plt.yscale('log')
    plt.xscale('log')
    plt.axis([0,(float(getMax(NestList_size_compaction))+500),0,(float(getMax(NestList_size_compaction))+500)])

    plt.plot([0,(float(getMax(NestList_size_compaction))+500)],[0,(float(getMax(NestList_size_compaction))+500)])    
    plt.xlabel("JSYN-VG w/ compaction")
    plt.ylabel("JSYN-VG")
    plt.title("Lines of Code")
    plt.legend(loc = 'upper left')
    fig.savefig("loccompact.pdf")

    #plt.yscale('log')
    #plt.ylim(pow(10,1), pow(10,3.5))
    #synthesized = plt.plot(pl1,'-r^', label = 'JSYN-VG w/ compaction', markersize = 10)
    #fixpoint = plt.plot(pl2,'-bo', label = 'JSYN-VG', markersize = 7)

    #plt.xlabel("Model")
    #plt.ylabel("Lines of Code")
    #plt.legend(loc = 'upper left')
    #fig.savefig("loc.pdf")


def main():
  drawFixpointReducedSize()
  drawSize()
  drawOverhead()
  drawPerformance()


main()