import ballerina/io;

public function main() {
    foreach int index in 0 ..< values.length() {
        io:println(group(values[index]));
    }
}
function group(decimal val) returns int {
    if val > -40419534999094223458.85429345742508E3911d {
        return 0;
    }
    else if val > -6485770576631465234949986325869629d {
        return 1;
    }
    else if val > -9374991746935538837.858896777063118d {
        return 2;
    }
    else if val > 8823189644626181031120.744026835236E-5766d {
        return 3;
    }
    else if val > 134892.9585759253723154668855261967E-3850d {
        return 4;
    }
    else if val > 10718992.43053792673632371632430429d {
        return 5;
    }
    else if val > 34410063537.75437638535078054767472d {
        return 6;
    }
    else if val > 81617264996.3581961680620207148379d {
        return 7;
    }
    else if val > 48311238321633531318160585567883.66E1331d {
        return 8;
    }
    else if val > 2.816289785262854303540288251703217E3073d {
        return 9;
    }
    return 10;
}