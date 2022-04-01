#!/usr/bin/perl

#use strict;
#use warnings;
#usage: perl Remove_SNPs_within_10bp.pl in.txt out.txt
#in.txt:sorted by chromsome and position
#chromsome	position
#chr1	123456
#chr1	123459
#chr2	123246
#chr2	123257

use Storable qw(dclone);

open(IN,"<","$ARGV[0]") or die "Can not open this file:$!";
open(OUT,">","$ARGV[1]") or die "Can not create this file:$!";

%hash={};
%new_hash={};

while(<IN>)
{
	chomp;
	(my $chr,my $pos)=split(/\t/,$_);
	push @{$hash{$chr}},"$pos";
}

my %new_hash = %{dclone(\%hash)};

foreach my $key (keys %hash)
{
	$num=(scalar(@{$hash{$key}}));
	if(($num>2))
	{
		foreach my $i (0 .. (scalar(@{$hash{$key}})-1))
		#foreach my $i (@{$hash{$key}})
		{
			#print OUT "$key: $hash{$key}[$i]\n";
			#print OUT "$key: $i\n";
			if ($hash{$key}[$i+1]-$hash{$key}[$i]<=10)
			{
				delete $new_hash{$key}[$i+1];
				$i=$i+1;
			}
			else
			{
				$i=$i+1;
			}
		}
	}
	elsif(($num==2))
	{
		if ($hash{$key}[1]-$hash{$key}[0]<=10)
		{
			delete $new_hash{$key}[1];
		}	
	}
	else
	{}
}

foreach my $key2 (keys %new_hash)
{
	foreach my $j (@{$new_hash{$key2}})
	{
		if (defined $j)
		{#print OUT "$key2:$new_hash{$key}\n";
			print OUT "$key2\t$j\n";
		}
	}
}

close IN;
close OUT;
