---
date: 2018-11-22 12:26:40
layout: main
title: Why books should be your priority?
subtitle: Lorem ipsum dolor sit amet, consectetur adipisicing elit.
description: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
image: https://res.cloudinary.com/dm7h7e8xj/image/upload/v1559822138/theme9_v273a9.jpg
optimized_image: https://res.cloudinary.com/dm7h7e8xj/image/upload/c_scale,w_380/v1559822138/theme9_v273a9.jpg
category: life
tags:
  - books
  - read
author: mranderson
paginate: true
---

{% assign gif_urls = site.data.gifs | strip_newlines | split: '\n' %}

{% if site.paginate %}
{% assign posts = paginator.posts | where_exp:"post","post.is_generated != true" %}
{% else %}
{% assign posts = site.posts | where_exp:"post","post.is_generated != true" %}
{% endif %}

{% if site.show_hero and paginator == nil or paginator.page == 1 %}
{% assign offset = 1 %}
{% else %}
{% assign offset = 0 %}
{% endif %}

<main class="home {% if site.show_hero and paginator == nil or paginator.page == 1 %}no-padding{% endif %}" role="main">
    {% if site.show_hero and paginator == nil or paginator.page == 1 %}
    <!-- Hero -->
    {% assign featured = posts.first %}
    <section class="hero"
        style="background-image: url('https://d.furaffinity.net/art/p4nd4art/1695345739/1695345739.p4nd4art_garticbanner.jpg')">
        <div class="pixels"></div>
        <div class="gradient"></div>
        <div class="content">
            <time datetime="{{ featured.date | date_to_xmlschema }}" class="date">
                {% if site.date_format == nil %}
                {{ featured.date | date: "%m.%d.%Y" }}
                {% else %}
                {{ featured.date | date: site.date_format }}
                {% endif %}
            </time>
            <h1 class="title">{{ featured.title }}</h1>
            <p class="description">{{ featured.subtitle }}</p>
            <div class="buttons">
                <button class="openLightboxBtn button" data-lightbox-id="heroLightbox">
                    <svg>
                        <use xlink:href="#icon-read"></use>
                    </svg>
                    <span>Credits</span>
                </button>
                <!--
                <a href="{{ featured.url | prepend: site.baseurl }}" role="button" class="button">
                    <svg>
                        <use xlink:href="#icon-read"></use>
                    </svg>
                    <span>{{ site.translations.button.read_now | default: "Made possible by the following people..."
                        }}</span>
                </a>
                -->
            </div>
        </div>
    </section>
    <!-- Edit Credits Here -->
    <div id="heroLightbox" class="lightbox">
        <div class="content">
            <h1 class="title">Thank you to everyone who contributed!</h1>
            <table class="description">
                <th class="subtitle" colspan="2"><br><br>Syndichat Developers</th>
                <tr>
                    <th>kimmu</th>
                    <th>kerro</th>
                </tr>
                <th class="subtitle" colspan="2"><br><br>Art Credit</th>
                <tr>
                    <th>ciniscinerem</th>
                    <th>ciniscinerem</th>
                </tr>
                <tr>
                    <th>trexcien</th>
                    <th>silvermoonwolf</th>
                </tr>
                <tr>
                    <th>akyren</th>
                    <th>zeiio.zeal</th>
                </tr>
                <tr>
                    <th>charlight</th>
                    <th>kimmu</th>
                </tr>
            </table>
            <th class="buttons" colspan="2">
                <button class="closeLightboxBtn button" data-lightbox-id="heroLightbox">
                    <svg>
                        <use xlink:href="#lightbox-close"></use>
                    </svg>
                    <span>Close</span>
                </button>
            </th>
        </div>
    </div>
    {% endif %}
    <!-- Posts -->
    <section id="grid" class="row flex-grid">
        {% for gif_url in gif_urls offset: offset %}
        <article class="box-item">
            <div class="box-body">
                <a class="cover" data-fancybox href="{{ gif_url }}" data-lightbox="img-gallery" data-title="GIF">
                    <!-- You can customize this part based on your needs -->
                    <img src="{{ gif_url }}" width="100%" class="preload">
                </a>
            </div>
        </article>
        {% endfor %}
    </section>
    <!-- Pagination -->
    {% if site.paginate %}
    {% include pagination-home.html %}
    {% endif %}
</main>


{% assign social_urls = '' %}
{% if site.github_username %}
{% assign social_urls = social_urls | append: '"https://github.com/' | append: site.github_username | append: '",' %}
{% endif %}
{% if site.facebook_username %}
{% assign social_urls = social_urls | append: '"https://www.facebook.com/' | append: site.facebook_username | append:
'",' %}
{% endif %}
{% if site.twitter_username %}
{% assign social_urls = social_urls | append: '"https://twitter.com/' | append: site.twitter_username | append: '",' %}
{% endif %}
{% if site.medium_username %}
{% assign social_urls = social_urls | append: '"https://medium.com/@' | append: site.medium_username | append: '",' %}
{% endif %}
{% if site.instagram_username %}
{% assign social_urls = social_urls | append: '"https://www.instagram.com/' | append: site.instagram_username | append:
'",' %}
{% endif %}
{% if site.linkedin_username %}
{% assign social_urls = social_urls | append: '"https://www.linkedin.com/in/' | append: site.linkedin_username | append:
'",' %}
{% endif %}

<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "WebPage",
  "mainEntity": {
    "@type": "Blog",
    "name": "{{ site.name }}",
    "headline": "{{ site.title }}",
    "description": "{{ site.description }}",
    "url": "{{ site.url }}{{site.baseurl}}/",
    "inLanguage": "{{ site.language }}",
    "isFamilyFriendly": "true",
    "creator": {
        "@type": "Organization",
        "name": "{{ site.name }}",
        "url": "{{ site.url }}{{site.baseurl}}/",
        "sameAs": [
            {{ social_urls | split: "," | join: "," }}
        ]
    },
    "mainEntity": {
        "@type": "ItemList",
        "itemListElement": [
        {% assign limit = 8 %}
        {% for post in posts limit: limit %}
            {% assign author = site.authors | where: "name", post.author | first %}
            {
                "@type": "BlogPosting",
                "name": "{{ post.title }}",
                "headline": "{{ post.subtitle }}",
                "description": "{{ post.description }}",
                "image": "{{ post.image }}",
                "url": "{{ post.url | prepend: site.baseurl | prepend: site.url }}",
                "inLanguage": "{{ site.language }}",
                "dateCreated": "{{ post.date | date: '%Y-%m-%d/' }}",
                "datePublished": "{{ post.date | date: '%Y-%m-%d/' }}",
                "dateModified": "{{ post.date | date: '%Y-%m-%d/' }}",
                "author": {
                    "@type": "Person",
                    "name": "{{ author.display_name }}",
                    "url": "{{ author.url | prepend: site.baseurl | prepend: site.url }}"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "{{ site.name }}",
                    "url": "{{ site.url }}{{site.baseurl}}/",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "{{ site.url }}{{site.baseurl}}/assets/img/blog-image.png",
                        "width": "600",
                        "height": "315"
                    }
                },
                "mainEntityOfPage": "True",
                "genre": "{{ post.category | capitalize }}",
		        "articleSection": "{{ post.category | capitalize }}",
                "keywords": [{{ post.tags | join: '","' | append: '"' | prepend: '"' }}]
            }{% if forloop.last == false  %},{% endif %}
        {% endfor %}
        ]
    }
  }
}
</script>