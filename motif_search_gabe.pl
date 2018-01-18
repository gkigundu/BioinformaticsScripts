use warnings;
use strict;

my $motif = '';
my $empty = "";
my @c;
my @array;
my $count = 0;

#change to what file your translated sequences are in also keep in mind this must
#be in the same location as the program otherwise it will not find the file
my $filename = 'test3_clean.fa';
my $outputPoreFilename = 'test_pore.fa';
my $outputVSDFilename = 'test_vsd.fa'; 
#Please save the beginning of sequence headers with >
#Also please save beginning of reading frames with #

#open file that you are reading from
if (open(my $fh, '<:encoding(UTF-8)', $filename)) {
	#go through each row from the file
	while (my $row = <$fh>) {
		chomp $row;		
		#remove the white spaces
		$row =~ s/\s//g;
		#search string for fasta character > # and save to array
		if($row =~ m/>/){
			push(@array, $row);
			push(@array, $empty);
			$count++;
			$count++;
		#}elsif($row =~ m/#/){
		#	push(@array, $row);
		#	$count++;
		}else{
			$array[$count - 1] = $array[$count - 1] . $row;
		}
	}
}
#define motif
$motif = '(T|S)(V|I)G(Y|F)G|(T|C)(L|Q|G|F|S)(S|E|D|K|A)(S|Y|E|G)W(E|A|S|I|M)|T(M|G|F)E(G|D|A)W(T|N|P|Q)';

#gives number of elements in array
my $num = @array;

#flag for printing sequences
my $flag = 0;

#secondary strings for headers
my $organism = '';
my $frame = '';

#indices to ignore
my $total =0;
# search the array of strings for motif 
if (open(my $poreFile, '>:encoding(UTF-8)', $outputPoreFilename) and open(my $vsdFile, '>:encoding(UTF-8)', $outputVSDFilename)){
	for(my $i = 0; $i <$num ;$i++){
		$_ = $array[$i];
		print $_, "\n";
		if($_ =~ m/>/){
			#my $result = index($_, '[');
			#$organism = substr($_,$result + 1,20);
			$organism = $_;
		}
		else{
			#if($_ =~ m/#/){
			#	$frame = substr($_,0,11);
			#}
			s{$motif}{
				# remember position
				push @c, pos;
				print "Position: ", pos, " Motif length", length($motif), "\n";
				$flag = 1;
				$total++;
			}eg;
	
			#if motif was found print partial header, number of times found, and location
			if($flag == 1){
				# print transformed string
				print "FOUND MOTIF IN: ".$organism."\n";
				print "NUMBER OF SITES THE MOTIF IS PRESENT IN: ".@c."\n";
				print "AND THE POSITION IN THE STRING IS: ", join(',', @c), "\n";
				#print "THE FRAME IS: ".$frame."\n\n";
				@c = ();
				#$organism = '';
				#$frame = '';
				$flag = 0;
				print $poreFile $organism , "\n";
				print $poreFile $_ , "\n";

			}else{
				print $vsdFile $organism , "\n";
				print $vsdFile $_, "\n";
				
			}
		}
	}
}
print "Total sequences: ", $count/2, "\n";
print "Pore domains: ", $total, "\n";
exit;
