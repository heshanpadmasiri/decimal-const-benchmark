import ballerina/io;

public function main() {
    decimal[] values = [1862159251048402173066781236007.325, -82595644.1772847817845744051143350, -8490854876241.565173798557846811177, -5437331953953436379082847.90425061, 52434197.04958126604279320284861946E-3453];
    foreach int index in 0 ..< values.length() {
        io:println(group(values[index]));
    }
}
function group(decimal val) returns int {
    if val > -26888089642524452921096875.8680100d {
        return 0;
    }
    else if val > -63512927983280920216500.85503563204d {
        return 1;
    }
    else if val > -3834851435458688.941430075854650172d {
        return 2;
    }
    else if val > -2840.284042049060777291366645267965d {
        return 3;
    }
    else if val > -645052286587311421.266198256528380E-4096d {
        return 4;
    }
    else if val > 9685448250894118.248350364705878727E-6130d {
        return 5;
    }
    else if val > 65814237821.17314391758517211501847d {
        return 6;
    }
    else if val > 456565485520681.6907694631930748203d {
        return 7;
    }
    else if val > 16827665420758159635395.65488882898E1276d {
        return 8;
    }
    else if val > 11677854665260013363100111.55261224E3352d {
        return 9;
    }
    return 10;
}
