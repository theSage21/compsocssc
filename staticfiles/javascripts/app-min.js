function setHeroHeight(){var t=$(window).height(),e=$("header").height();$("#hero").height(t-e)}!function($){$.fn.fitText=function(t,e){var n=t||1,i=$.extend({minFontSize:Number.NEGATIVE_INFINITY,maxFontSize:Number.POSITIVE_INFINITY},e);return this.each(function(){var t=$(this),e=function(){t.css("font-size",Math.max(Math.min(t.width()/(10*n),parseFloat(i.maxFontSize)),parseFloat(i.minFontSize)))};e(),$(window).on("resize.fittext orientationchange.fittext",e)})}}(jQuery),$(document).ready(function(){setHeroHeight(),$("#arrow").on("click",function(){$("html, body").animate({scrollTop:$("#upcoming-event").offset().top},900),$(this).fadeOut("slow")}),$("#upcoming-event .content h1").fitText(),$("#upcoming-event .content h2").fitText({maxFontSize:"5em"})});